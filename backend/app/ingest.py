from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()


def ingest_documents():
    loader = PyPDFLoader("data/tcs_document.pdf")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_documents(texts, embeddings)

    vectorstore.save_local("faiss_index")

    print("✅ Documents indexed successfully!")


if __name__ == "__main__":
    ingest_documents()