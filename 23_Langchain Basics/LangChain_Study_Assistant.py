# from langchain_ollama import OllamaLLM
# from langchain.prompts import PromptTemplate
# from langchain_community.chat_message_histories import ChatMessageHistory
# import json
# from datetime import datetime

# class StudyAssistant:
#     def __init__(self,subject="Python"):
#         self.__subject = subject
#         self.__llm = OllamaLLM(model="llama3.2")
#         self.__history = []
#         self.__notes = []

#         self.__templates = {
#             "explain":PromptTemplate(
#                 input_variables=["topic","subject"],
#                 template="""
# You are a {subject} teacher.
# Explain it under 150 words.
# """
#             ),
#             "quiz":PromptTemplate(
#                 input_variables=['topic'],
#                 template ="""
# Create 3 multiple choice questions about {topic}.
# Format: Q1, options A/B/C/D, correct answer.
# """
#             ),
#             "summary":PromptTemplate(
#                 input_variables=["notes"],
#                 template="""
# Summarize these study notes in 5 bullet points:
# {notes}
# """
#             )
#         }
#     def explain(self,topic):
#         prompt = self.__templates["explain"].format(
#             topic = topic,
#             subject= self.__subject
#         )
#         response = self.__llm.invoke(prompt)

#         self.__notes.append({
#             "topic":topic,
#             "explanation":response,
#             "timestamp":datetime.now().strftime("%H:%M")
#         })
#         print(f"\n📖 {topic}")
#         print(response)
#     def quiz(self,topic):
#         prompt = self.__templates["quiz"].format(topic=topic)
#         response = self.__llm.invoke(prompt)
#         print(f"\n❓ Quiz - {topic}:")
#         print(response)
#     def summarize(self):
#         if not self.__notes:
#             print("❌ Please explain something!")
#             return
#         all_notes = "\n".join([
#             f"{n['topic']}:{n['explanation'][:100]}" for n in self.__notes
#         ])
#         prompt=self.__templates["summmary"].format(notes=all_notes)
#         response = self.llm.invoke(prompt)
#         print(f"\n📖 Session Summary:")
#         print(response)
#     def save_notes(self):
#         filename = f"study_notes_{datetime.now().strftime('%Y%m%d')}.json"
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(self.__notes,f,indent=4, ensure_ascii=False)
#         print(f"✅ Notes Saved: {filename}")
#     def run(self):
#         print(f"📖 Study Assistant - {self.__subject}")
#         print("Commands: explain, quiz, summary, save, quit")
#         print("-"*45)
#         while True:
#             command = input("\n> ").strip().lower()
#             if command == "quit":
#                 print("👋 Keep Learning!")
#             elif command == "explain":
#                 topic = input("Topic: ").strip()
#                 self.explain(topic)
#             elif command == "quiz":
#                 topic = input("Topic:" ).strip()
#                 self.quiz(topic)
#             elif command == "summary":
#                 self.summarize()
#             elif command == "save":
#                 self.save_notes()
#             else: 
#                 print("❌ Commands: explain/quiz/summary/save/quit")
# assistant = StudyAssistant("Python & AI")
# assistant.run()

import os
import json
from datetime import datetime
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
class StudyAssistant:
    def __init__(self,subject="Python"):
        self.__subject = subject
        self.__llm = ChatGroq(model="gpt-oss-20b",temperature=0.3) #Model may be change with time to time so use latest model
        self.__parser = StrOutputParser()
        self.__notes = []

        self.__templates = {
            "explain":PromptTemplate(
                input_variables=["topic","subject"],
                template="""
You are a {subject} teacher.
Explain {topic} in simple terms with one short code example.
Keep it under 150 words. Hinglish mix is fine.
"""
            ),
            "quiz":PromptTemplate(
                input_variables=["topic"],
                template="""
Create 3 Mulitple choice questions about {topic}.
Format: Q1, options A/B/C/D, correct answer at the bottom.
"""
            ),
            "summary":PromptTemplate(
                input_variables=["notes"],
                template="""
Summarize these study notes in 5 clear bullet points:
{notes}
"""
            )
        }
    def explain(self,topic):
        chain = self.__templates["explain"] | self.__llm | self.__parser 
        response = chain.invoke({"topic":topic,"subject":self.__subject})

        self.__notes.append({
            "topic":topic,
            "explanation":response,
            "timestamp":datetime.now().strftime("%H:%M")
        })
        print(f"\n📖 {topic}:")
        print(response)
    def quiz(self,topic):
        chain = self.__templates["quiz"] | self.__llm | self.__parser
        response = chain.invoke({"topic":topic})
        print(f"\n❓ Quiz - {topic}:")
        print(response)
    def summarize(self):
        if not self.__notes:
            print("❌ Please explain some topic first.")
            return 
        all_notes = "\n".join([
            f"Topic:{n['topic']}\nContent: {n['explanation'][:150]}..." for n in self.__notes 
        ])
        chain = self.__templates["summary"] | self.__llm | self.__parser
        response = chain.invoke({"notes":all_notes})
        print(f"\nSession Summary:")
        print(response)
    def save_notes(self):
        filename = f"groq_study_notes_{datetime.now().strftime('%Y%m%d')}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.__notes, f, indent=4, ensure_ascii=False)
        print(f"✅ Notes saved successfully: {filename}")
    def run(self):
        print(f"📚 AI Cloud Study Assistant - {self.__subject}")
        print("Commands: explain, quiz, summary, save, quit")
        print("-"*50)

        while True:
            command = input("\n> ").strip().lower()

            if command == "quit":
                print("👋 Keep learning! Allah Hafiz.")
                break
            elif command == "explain":
                topic = input("Topic name: ").strip()
                self.explain(topic)
            elif command == "quiz":
                topic = input("Topic name: ").strip()
                self.quiz(topic)
            elif command == "summary":
                self.summarize()
            elif command == "save":
                self.__save_notes()
            else:
                print("❌ Wrong Command! Use: explain, quiz, summary, save, quit")
# Run the app
if __name__ == "__main__":
    if not os.getenv("GROQ_API_KEY"):
        print("❌ Error: Could not find GROQ_API_KEY. Look at '.env' file whether it is correct or not.")
    else:
        assistant = StudyAssistant("Machine Learning & Python")
        assistant.run()