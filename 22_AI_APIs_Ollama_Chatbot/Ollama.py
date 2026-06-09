import requests
import json
class OllamaClient:
    def __init__(self,model="llama3.2"):
        self.model = model
        self.__base_url = "http://localhost:11434"
    def chat(self, message):
        try:
            response = requests.post(
                f"{self.__base_url}/api/generate",
                json={
                    "model":self.model,
                    "prompt":message,
                    "stream":False
                },
                timeout=60
            )
            response.raise_for_status()
            return response.json()['response']
        except requests.exceptions.ConnectionError:
            return "❌ Ollama is not working - Please run 'ollama server!' "
        except Exception as e:
            return f"❌ Error: {e}"
    def chat_with_context(self,messages):
        # messages = [{"role":"user/assistant", "content":"....."}]
        try:
            response = requests.post(
                f"{self.__base_url}/api/chat",
                json={
                    "model":self.model,
                    "messages":messages,
                    "stream":False
                },
                timeout=60
            )
            return response.json()["message"]["content"]
        except Exception as e:
            return f"❌ Error: {e}"
client = OllamaClient()
response = client.chat("What is decorator in Python? Explain in 2 lines")
print(response)