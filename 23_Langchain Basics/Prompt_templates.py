# # Prompt Templates - Dynamic Prompts
# from langchain_ollama import OllamaLLM
# from langchain_core.prompts import PromptTemplate
# llm = OllamaLLM(model="llama3.2")
# template = PromptTemplate(
#     input_variables=["topic","level"],
#     template="""
# You are teaching {level} level student {topic}.
# Tell 3 main key points in simple language.
# """
# )
# prompt1 = template.format(topic="OOP",level="beginner")
# prompt2 = template.format(topic="LangChain",level="intermediate")
# print(llm.invoke(prompt1))
# print(llm.invoke(prompt2))

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant") #Model may be change with time to time so use latest model
template = PromptTemplate(
    input_variables=["topic","level"],
    template="""
You are teaching {level} level student {topic}.
Tell 3 main key points in simple language
"""
)
prompt1 = template.format(topic="OOP",level="beginner")
prompt2 = template.format(topic="LangChain",level="intermediate")
print(llm.invoke(prompt1).content)
print(llm.invoke(prompt2).content)