import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.tools import StructuredTool
from Business_Chatbot.rag import RAGSystem
from Business_Chatbot.tools import get_current_time, save_lead, calculate_project_cost

load_dotenv()

class BusinessAgent:
    def __init__(self):
        # Groq Cloud LLM
        self.__llm = ChatGroq(
            model="llama-3.3-70b-versatile", 
            temperature=0.2,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        self.__rag = RAGSystem()
        
        # Tools Wrap karna for Structured Handling
        self.__tools = [
            StructuredTool.from_function(func=get_current_time, name="get_current_time", description="Get current date and time."),
            StructuredTool.from_function(func=save_lead, name="save_lead", description="Save customer lead info. Input: name, email, service"),
            StructuredTool.from_function(func=calculate_project_cost, name="calculate_project_cost", description="Calculate estimated cost for project type: chatbot, scraping, dashboard, agent")
        ]
        
        # Native Tool Binding to LLM (Token Saver & High Speed)
        self.__tools_map = {tool.name: tool for tool in self.__tools}
        self.__llm_with_tools = self.__llm.bind_tools(self.__tools)
        
        self.__prompt_template = PromptTemplate(
            input_variables=["context", "question"],
            template="""
            You are a professional business assistant for TechSolve Pakistan.
            Always be helpful, professional, and concise.
            
            Company Information:
            {context}
            
            Customer Question: {question}
            
            Provide a helpful, professional response based on 
            the company information above.
            """
        )
    
    def setup(self):
        return self.__rag.load_documents()
    
    def respond(self, question):
        # 1. RAG se Context extract karo
        context = self.__rag.get_context(question)
        
        # 2. Query ko context ke sath enhance karo for LLM
        prompt_text = self.__prompt_template.format(
            context=context,
            question=question
        )
        
        try:
            # 3. Native Tool-calling LLM Invoke
            ai_msg = self.__llm_with_tools.invoke(prompt_text)
            
            # Agar LLM ne decide kiya ke tool chalana hai (e.g. Lead Save, Price Calculation, Time)
            if ai_msg.tool_calls:
                tool_results = []
                for tool_call in ai_msg.tool_calls:
                    tool_name = tool_call["name"]
                    tool_args = tool_call["args"]
                    
                    selected_tool = self.__tools_map[tool_name]
                    arg_val = list(tool_args.values())[0] if tool_args else ""
                    
                    output = selected_tool.run(arg_val)
                    tool_results.append(output)
                
                return "\n".join(tool_results)
            
            # Agar koi tool ki zarurat nahi, direct RAG answer return karo
            return ai_msg.content
            
        except Exception as e:
            return f"❌ Error: {e}"