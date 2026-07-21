import os
from dotenv import load_dotenv

# LangSmith aur baki warnings ko run-time se pehle hi block karne ke liye
os.environ["LANGSMITH_TRACING"] = "false"
os.environ["LANGCHAIN_TRACING_V2"] = "false"

from langchain_core.tools import StructuredTool
from langchain_groq import ChatGroq
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# Environment variables load karein
load_dotenv()

# ============ DEFINE FUNCTIONS ============

def calculator(expression: str) -> str:
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"

def word_counter(text: str) -> str:
    words = len(text.split())
    chars = len(text)
    sentences = text.count('.') + text.count('!') + text.count('?')
    return f"Words: {words}, Characters: {chars}, Sentences: {sentences}"

def grade_calculator(marks: str) -> str:
    try:
        marks_list = [float(m.strip()) for m in marks.split(',')]
        avg = sum(marks_list) / len(marks_list)
        
        if avg >= 80: grade = "A"
        elif avg >= 70: grade = "B"
        elif avg >= 60: grade = "C"
        elif avg >= 50: grade = "D"
        else: grade = "F"
        
        return f"Average: {avg:.1f}%, Grade: {grade}"
    except Exception as e:
        return f"Error: {e}"

# ============ EXPLICIT TOOL WRAPPING (FAIL-SAFE) ============
# Yeh step LangChain ko majboor karega ke woh isko real object hi mane

calculator_tool = StructuredTool.from_function(
    func=calculator,
    name="calculator",
    description="Mathematical calculations karo. Input: math expression jaise '2 + 2' ya '15 * 4'"
)

word_counter_tool = StructuredTool.from_function(
    func=word_counter,
    name="word_counter",
    description="Text mein words aur characters count karo. Input: koi bhi text string"
)

grade_calculator_tool = StructuredTool.from_function(
    func=grade_calculator,
    name="grade_calculator",
    description="Marks se grade calculate karo. Input: comma separated marks jaise '85,90,78,92'"
)

# Tools list
tools = [calculator_tool, word_counter_tool, grade_calculator_tool]

# ============ GROQ AGENT INITIALIZATION ============
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Standard ReAct Prompt pull karein langchain hub se
prompt = hub.pull("hwchase17/react")

# Agent aur Executor build karein
agent_runnable = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent_runnable, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors=True
)

# Test karo:
if __name__ == "__main__":
    print("\n🤖 Running Groq Agent...")
    result = agent_executor.invoke({"input": "85, 92, 78, 95 ka average aur grade kya hoga?"})
    print("\nFINAL OUTPUT:")
    print(result["output"])