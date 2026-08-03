import streamlit as st
from Business_Chatbot.agent import BusinessAgent

st.set_page_config(
    page_title="TechSolve AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# Agent initialize — sirf ek baar
@st.cache_resource
def load_agent():
    agent = BusinessAgent()
    agent.setup()
    return agent

st.title("🤖 TechSolve Pakistan")
st.subheader("AI Customer Support Assistant")
st.markdown("---")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Assalam o Alaikum! Main TechSolve ka AI assistant hoon. Kaise help kar sakta hoon?"
        }
    ]

# Chat display
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Apna sawal poochein..."):
    
    # User message show karo
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    with st.chat_message("user"):
        st.write(prompt)
    
    # AI response lo
    with st.chat_message("assistant"):
        with st.spinner("Soch raha hoon..."):
            agent = load_agent()
            response = agent.respond(prompt)
            st.write(response)
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.info("Powered by RAG + AI Agents + Ollama")
    st.markdown("---")
    st.markdown("**Ask me about:**")
    st.markdown("- Our services & pricing")
    st.markdown("- Project timelines")
    st.markdown("- Contact information")
    st.markdown("- Getting a quote")