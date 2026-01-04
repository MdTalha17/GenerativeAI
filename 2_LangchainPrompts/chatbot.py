from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-3.5-turbo")
messages = [
        SystemMessage(content="You are a helpful assistant.")
    ]

while True:
    user_input = input("You: ")
    messages.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break

    result = model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print("Assistant: ", result.content)

print(messages)