from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatGoogleGenerativeAI(model_name="gemini-2.0-flash-exp", temperature=1)

reply = chat.invoke("Hello, how are you?")

print(reply.content)
