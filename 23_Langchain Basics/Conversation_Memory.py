# from langchain_ollama import OllamaLLM
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.chat_history import InMemoryChatMessageHistory
# from langchain_core.runnables import RunnableWithMessageHistory
# # from langchain_community.chat_message_histories import ChatMessageHistory

# llm = OllamaLLM(model="llama3.2")
# #Memory Store
# store = {}
# def get_session_history(session_id):
#     if session_id not in store:
#         store[session_id] = InMemoryChatMessageHistory()
#     return store[session_id]
# prompt = ChatPromptTemplate.from_messages([
#     ("system","You are a helpful Python teacher."),
#     MessagesPlaceholder(variable_name="history"),
#     ("human","{input}")
# ])

# chain = prompt | llm
 
# # Memory ke saath chain
# chain_with_memory = RunnableWithMessageHistory(
#     chain,
#     get_session_history,
#     input_messages_key="input",
#     history_messages_key="history"
# )
# # Conversation karo
# r1 = chain_with_memory.invoke(
#     {"input":"What is OOP?"},
#     config={"configurable":{"session_id":"hassan_session"}}
# )
# print(f"AI: {r1}")

# r2 = chain_with_memory.invoke(
#     {"input":"Give the example of what you describe first."},
#     config={"configurable":{"session_id":"hassan_session"}}
# )
# print(f"AI; {r2}")

# For external APIs
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant")  #Model may be change with time to time so use latest model
store = {}
def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]
prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful Python Teacher."),
    MessagesPlaceholder(variable_name="history"),
    ("human","{input}")
])
chain = prompt | llm
chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)
r1 = chain_with_memory.invoke(
    {"input":"What is OOP?"},
    config={"configurable":{"session_id":"hassan_session"}}
)
print(f"AI: {r1.content}\n")
r2 = chain_with_memory.invoke(
    {"input":"Give me small code example of what you teach first."},
    config={"configurable":{"session_id":"hassan_session"}}
)
print(f"AI: {r2.content}")