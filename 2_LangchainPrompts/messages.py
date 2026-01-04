## Messages are used to make chatbots

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-3.5-turbo")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello!!")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)