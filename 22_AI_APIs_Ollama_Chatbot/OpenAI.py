# # This code is for Open AI 
# import requests
# class AIClient:
#     def __init__(self, api_key, model="gpt-3.5-turbo"):
#         self.__api_key = api_key
#         self.model = model
#         self.__url = "https://api.openai.com/v1/chat/compltions"
#         self.__headers = {
#             "Authorization":f"Bearer {self.__api_key}",
#             "api-key":self.__api_key,
#             "Content-Type":"application/json"
#         }
#         self.__headers = {"Content-Type":"application/json"}
#     def chat(self,message, system_prompt=None):
#         messages = []
#         if system_prompt:
#             messages.append({
#                 "role":"system",
#                 "content":system_prompt
#             })
#         messages.append({
#             "role":"user",
#             "content":message
#         })
#         try:
#             response = requests.post(
#                 self.__url,
#                 headers=self.__headers,
#                 json={
#                     "model":self.model,
#                     "messages":messages,
#                     "max_tokens":500
#                 },
#                 timeout=30
#             )
#             response.raise_for_status()
#             return response.json()["choices"][0]["message"]["content"]
#         except Exception as e:
#             return f"❌ Error: {e}"



# This code is for Gemini free API Key
import requests
class AIClient:
    def __init__(self, api_key, model="gemini-2.0-flash-lite"):
        self.__api_key = api_key
        self.model = model
        self.__url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.__api_key}"
        self.__headers = {"Content-Type":"application/json"}
    def chat(self,message):
        payload = {
            "contents":[{
                "parts":[{"text":message}]
            }]
        }
        try:
            response = requests.post(self.__url,headers=self.__headers,json=payload,timeout=30)
            if response.status_code != 200:
                return f"❌ HTTP Error {response.status_code}:{response.text}"
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            print(response.status_code)
            print(response.text)
            print(e)
            # return f"❌ Error: {e}"
GEMINI_FREE_KEY = "YOUR GEMINI KEY"
client = AIClient(api_key=GEMINI_FREE_KEY)
reply = client.chat("What are Generators in python? Explain in one line.")
print(reply)