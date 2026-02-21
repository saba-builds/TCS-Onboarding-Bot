from app.rag_chain import create_rag_chain


def main():
    chain = create_rag_chain()

    print("🤖 TCS RAG Chatbot")
    print("Type 'exit' to quit\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            break

        response = chain.invoke(query)

        print("\nAnswer:", response)
        print("\n" + "-" * 50)


if __name__ == "__main__":
    main()