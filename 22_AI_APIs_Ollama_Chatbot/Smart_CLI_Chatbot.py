import requests
import json
from datetime import datetime
class SmartChatbot:
    def __init__(self,name="Hassan's AI",model="llama3.2"):
        self.name = name
        self.__model = model
        self.__base_url = "http://localhost:11434"
        self.__history = []
        self.__system_prompt = """You are a helpful assistant for 
        Hassan, a CS Student learning AI Automation Engineering.
        Keep answers concise and practical.
        When explaining code, use simple examples."""
    def __send(self,user_message):
        self.__history.append({
            "role":"user",
            "content":user_message
        })
        try:
            response = requests.post(
                f"{self.__base_url}/api/chat",
                json={
                    "model":self.__model,
                    "messages":[
                        {"role":"system","content":self.__system_prompt}
                    ] + self.__history,
                    "stream":False
                },
                timeout=60
            )
            ai_response = response.json()["message"]["content"]
            self.__history.append({
                "role":"assistant",
                "content":ai_response
            })
            return ai_response
        except requests.exceptions.ConnectionError:
            return "❌ Please Start Ollama Server: 'ollam server' "
        except Exception as e:
            return f"❌ Error: {e}"
    def save_history(self):
        filename = f"chat_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
        with open(filename,"w", encoding="utf-8") as f:
            json.dump({
                "bot_name":self.name,
                "saved_at":datetime.now().strftime("%Y-%m-%d_%H%M"),
                "conversation":self.__history
            }, f, indent=4, ensure_ascii=False
            )
            print(f"✅ Chat saved: {filename}")
    def show_history(self):
        if not self.__history:
            print(f"❌ There is not conversation yet!")
            return 
        print(f"\n{'='*50}")
        print(f" 💬 Conversation History")
        print(f"{'='*50}")
        for msg in self.__history:
            role = "You" if msg["role"] == "user" else "AI"
            print(f"\n{role}:\n {msg['content'][:100]}...")
    def run(self):
        print(f"{self.name} - Powered by Ollama")
        print("Commands: 'save', 'history', 'clear', 'quit'")
        print(f"{'-'*50}")
        while True:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue
            elif user_input.lower() == 'quit':
                print("👋 Allah Hafiz!")
                break
            elif user_input.lower() == "save":
                self.save_history()
            elif user_input.lower() == "history":
                self.show_history()
            elif user_input.lower() == "clear":
                self.__history = []
                print("✅ History Cleared!")
            else:
                print("\n AI: ",end="",flush=True)
                response = self.__send(user_input)
                print(response)
bot = SmartChatbot()
bot.run()
            