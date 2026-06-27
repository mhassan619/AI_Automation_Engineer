#For local, use ollama
# from langchain_ollama import OllamaLLM
# from langchain_core.prompts import PromptTemplate
# from langchain_core.runnables import RunnablePassthrough
# llm = OllamaLLM(model="llama3.2")

# #Chain 1 - Topics Explain kro
# explain_prompt = PromptTemplate(
#     input_variables=["topic"],
#     template="Explain {topic} in 3 simple points."
# )

# #Chain 2 - Quiz banao
# quiz_prompt = PromptTemplate(
#     input_variables=["explanation"],
#     template="""
# Based on this explanation:
# {explanation}
# Create 2 simple quiz questions.
# """
# )

# # Dono chain connect kro
# explain_chain = explain_prompt | llm
# quiz_chain = quiz_prompt | llm

# # Run Karo
# explanation = explain_chain.invoke({"topic":"Python Decorators"})
# print("Explanation")
# print(explanation)

# quiz = quiz_chain.invoke({"explanation":explanation})
# print("\n❓ Quiz: ")
# print(quiz)

# For external API like groq
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant")  #Model may be change with time to time so use latest model
output_parser = StrOutputParser()
explain_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in 3 simple points."
)
quiz_prompt = PromptTemplate(
    input_variables=["explanation"],
    template="Based on this explanation:\n{explanation}\n\nCreate 2 simple quiz questions."
)
# Make chains
explain_chain = explain_prompt | llm | output_parser
quiz_chain = quiz_prompt | llm | output_parser

# Now Run 
explanation = explain_chain.invoke({"topic":"Python Decorators"})
print("📖 Explanation: \n",explanation)
quiz = quiz_chain.invoke({"explanation":explanation})
print("\n❓ Quiz:\n",quiz)