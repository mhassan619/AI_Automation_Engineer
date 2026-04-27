import streamlit as st
st.set_page_config(
    page_title="Hassan's AI Dashboard",
    page_icon="📻",
    layout="wide"
)
st.title("📻 Hassan's AI Automation Dashboard")
st.subheader("My 3 AI Automation Real World Projects - All in One!")

st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("### 🙅‍♂️ GitHub Analyzer\nAnalyze any GitHub profile")
with col2:
    st.success("### 🌤️ Weather App\nReal-time weather data")
with col3:
    st.warning("### 📚 Book Scrapper\nBooks data visualization")
st.markdown("---")
st.caption("Built with Python + Streamlit | AI Automation Engineer in Progress")