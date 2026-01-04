from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0)

reply = llm.invoke("What is the capital of India?")

print(reply)
