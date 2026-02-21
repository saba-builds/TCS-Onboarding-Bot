from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


def create_rag_chain():
    # Load embeddings
    embeddings = OpenAIEmbeddings()

    # Load vector store
    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever()

    # LLM
    llm = ChatOpenAI(temperature=0)

    # Prompt
    prompt = ChatPromptTemplate.from_template("""
    You are a helpful TCS assistant.
    Answer the question using only the context below.
    If you don't know, say you don't know.

    Context:
    {context}

    Question:
    {question}
    """)

    # LCEL RAG pipeline
    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain