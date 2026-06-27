import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
llm = ChatGroq(
    model="gpt-oss-20b",  #Model may be change with time to time so use latest model
    temperature=0.7
)
response = llm.invoke("What is Python? Tell me in 2 lines.")
print(response.content)

##for local server use ollama 
# from langchain_ollama import OllamaLLM
# llm = OllamaLLM(model="llama3.2")
# response = llm.invoke("What is Python? Tell me in 2 lines.")
# print(response)