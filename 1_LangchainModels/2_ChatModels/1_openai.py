from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model_name="gpt-4", temperature=1, max_completion_tokens=10)

reply = chat.invoke("Hello, how are you?")

print(reply.content)