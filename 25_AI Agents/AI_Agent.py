import os
import json
from datetime import datetime
from dotenv import load_dotenv

# Tracing disable taake extra API calls na hon
os.environ["LANGSMITH_TRACING"] = "false"
os.environ["LANGCHAIN_TRACING_V2"] = "false"

from langchain_core.tools import StructuredTool
from langchain_groq import ChatGroq

load_dotenv()

# ============ DEFINE RAW FUNCTIONS ============

def save_note(note: str) -> str:
    try:
        notes = []
        if os.path.exists("agent_notes.json"):
            with open("agent_notes.json", "r") as f:
                notes = json.load(f)
        
        notes.append({
            "note": note,
            "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        
        with open("agent_notes.json", "w") as f:
            json.dump(notes, f, indent=4)
        
        return f"✅ Note saved! Total notes: {len(notes)}"
    except Exception as e:
        return f"❌ Error: {e}"


def read_notes(query: str) -> str:
    try:
        if not os.path.exists("agent_notes.json"):
            return "❌ Abhi koi notes nahi hain!"
        
        with open("agent_notes.json", "r") as f:
            notes = json.load(f)
        
        if query.lower() == "all" or not query:
            result = f"Total {len(notes)} notes:\n"
            for i, n in enumerate(notes, 1):
                result += f"\n{i}. {n['note'][:80]}..."
            return result
        
        matches = [n for n in notes if query.lower() in n['note'].lower()]
        if not matches:
            return f"'{query}' se koi note nahi mila!"
        
        result = f"{len(matches)} notes mile:\n"
        for n in matches:
            result += f"\n- {n['note'][:100]}"
        return result
    except Exception as e:
        return f"❌ Error: {e}"


def calculate_gpa(grades: str) -> str:
    grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    try:
        clean_input = grades.upper()
        grade_list = [char for char in clean_input if char in grade_points]
        if not grade_list:
            return "❌ Koi valid grades (A, B, C, D, F) nahi mile."
        points = [grade_points[g] for g in grade_list]
        cgpa = sum(points) / len(points)
        return f"Grades: {grade_list}\nCGPA: {cgpa:.2f}/4.0"
    except Exception as e:
        return f"❌ Error: {e}"


def topic_quiz(topic: str) -> str:
    questions = {
        "oop": ["Q1: OOP ke 4 pillars kya hain?", "Q2: Inheritance aur Composition mein farq?", "Q3: Abstract class ka object kyun nahi banta?"],
        "python": ["Q1: List aur Tuple mein kya farq hai?", "Q2: *args aur **kwargs kya hain?", "Q3: Generator aur normal function mein farq?"],
        "api": ["Q1: GET aur POST mein farq?", "Q2: Status code 401 aur 404 kya matlab?", "Q3: API key kyun use karte hain?"]
    }
    topic_lower = topic.lower()
    for key in questions:
        if key in topic_lower:
            return "\n".join(questions[key])
    return "OOP, Python, ya API mein se kisi ek topic ka naam batao taake main quiz generate kar sakoon."


# ============ EXPLICIT TOOLS MAP ============

save_note_tool = StructuredTool.from_function(func=save_note, name="save_note", description="Use this to save a study note. Input: exact note text.")
read_notes_tool = StructuredTool.from_function(func=read_notes, name="read_notes", description="Use this to search or read saved notes. Input: search keyword or 'all'.")
calculate_gpa_tool = StructuredTool.from_function(func=calculate_gpa, name="calculate_gpa", description="Use this to calculate CGPA. Input: comma separated grades like 'A,B,A'.")
topic_quiz_tool = StructuredTool.from_function(func=topic_quiz, name="topic_quiz", description="Use this to generate a quiz on programming topics. Input: 'oop', 'python', or 'api'.")

# Dictionary taake dynamic invoke kiya ja sakay
tools_map = {
    "save_note": save_note_tool,
    "read_notes": read_notes_tool,
    "calculate_gpa": calculate_gpa_tool,
    "topic_quiz": topic_quiz_tool
}


# ============ SMART AI ROUTER AGENT ============

class StudyAgent:
    def __init__(self):
        # Base LLM jise hum tools ki knowledge bind karenge
        self.__llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.3,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        # LLM ko tools ke baare mein batana (Native Tool Binding)
        self.__llm_with_tools = self.__llm.bind_tools(list(tools_map.values()))
        
    def run(self):
        print("🤖 Pure AI Study Agent (Native Tool Calling Mode)")
        print("=" * 50)
        print("Hassan parhaye! LLM khud sochega aur tool run karega.")
        print("-" * 50)
        
        while True:
            user_input = input("\n👤 You: ").strip()
            
            if not user_input:
                continue
            elif user_input.lower() == "quit":
                print("👋 Keep Learning Hassan!")
                break
                
            try:
                print("\n🤖 Agent: ", end="", flush=True)
                
                # 1. Single LLM Call: Model pure message ko dekh kar decide karega kya karna hai
                ai_msg = self.__llm_with_tools.invoke(user_input)
                
                # 2. Check agar LLM ne koi Tool select kiya hai
                if ai_msg.tool_calls:
                    for tool_call in ai_msg.tool_calls:
                        tool_name = tool_call["name"]
                        tool_args = tool_call["args"]
                        
                        # Dynamic execution: Jo tool LLM ne choose kiya, wahi chalega
                        selected_tool = tools_map[tool_name]
                        
                        # tool_args dictionary hoti hai, iska pehla value function ko pass kar do
                        argument_value = list(tool_args.values())[0] if tool_args else ""
                        
                        tool_output = selected_tool.run(argument_value)
                        print(tool_output)
                
                # 3. Agar koi tool select nahi hua, toh LLM ka direct normal reply
                else:
                    print(ai_msg.content)
                    
            except Exception as e:
                print(f"❌ Error: {e}")

if __name__ == "__main__":
    agent = StudyAgent()
    agent.run()