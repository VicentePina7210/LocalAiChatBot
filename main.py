from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below

Here is the conversation history: {context}

Question: {question}

Answer: 

"""

model = OllamaLLM(model = "llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to Local AI Chatbot! type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break

        result = chain.invoke({"context": context, "question": user_input})
        print("AI ", result)

        context += f"User: {user_input}\nAI: {result}\n"


if __name__ == "__main__":
    handle_conversation()