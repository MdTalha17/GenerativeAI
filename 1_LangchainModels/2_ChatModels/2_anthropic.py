from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chat = ChatAnthropic(model_name="claude-3-5-sonnet", temperature=1)

reply = chat.invoke("Hello, how are you?")

print(reply.content)