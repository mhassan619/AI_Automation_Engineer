from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()
class PDFChatbot:
    def __init__(self,model="llama-3.1-8b-instant"):
        self.__llm = ChatGroq(model=model,temperature=0.2)
        self.__embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.__vectorstore = None
        self.__pdf_loaded = False
        self.__chat_history = []
        self.__prompt = PromptTemplate(
            input_variables=["context","question","history"],
            template="""
            Tum eik helpful assistant ho jo sirf 
            provided documents ki information use krta hai.
            
            Previous Conversation:
            {history}

            Document Context:
            {context}

            User Question: {question}

            Instructions: 
            - Sirf document mein jo hai wo batao
            - Agr document mein ni hai to clearly kaho "Mujhy afsos hai, mere pass iski maloomat ni hai"
            - Simple aur clear jawab do (Roman Urdu/Mix English chalega)

            Answer:
            """
        )
    def load_pdf(self,pdf_path):
        if not os.path.exists(pdf_path):
            print(f"PDF nh milli {pdf_path}")
            return 
        print(f"📄 PDF load ho rahi hai: {pdf_path}")

        # Step 1: PDF Load karo
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()
        print(f"✅ {len(pages)} pages loaded!")

        # Step 2: Text chunks mein divide karo
        Splitter = RecursiveCharacterTextSplitter(
            chunk_size =500,
            chunk_overlap =50
        )
        chunks = Splitter.split_documents(pages)
        print(f"✅ {len(chunks)} chunks banaye!")

        # Step 3: Embeddings banao aur store karo (Chroma DB)
        print("🔄 Embeddings ban rahi hain...")
        self.__vectorstore = Chroma.from_documents(
            documents = chunks,
            embedding=self.__embeddings,
            persist_directory="./chroma_db"
        )

        self.__pdf_loaded = True
        print("✅ PDF ready hai — ab poochho!")
        return True
    def __get_context(self,question,k=3):
        if not self.__vectorstore:
            return ""
        
        # Question se related chunks nikalo
        relevant_docs = self.__vectorstore.similarity_search(
            question, k=k
        )
        context = "\n\n".join([
            f"[Page {doc.metadata.get('page', '?')}]: {doc.page_content}"
            for doc in relevant_docs
        ])
        return context
    def __formatted_history(self):
        if not self.__chat_history:
            return "No previous Conversation."
        formatted = []
        for msg in self.__chat_history[-4:]:
            role = "User" if msg["role"] == "user" else "Assistant"
            formatted.append(f"{role}: {msg['content'][:100]}")
        return "\n".join(formatted)
    
    def ask(self,question):
        if not self.__pdf_loaded:
            return "Pehle PDF Load kro!"
        # Context retrieve karo
        context = self.__get_context(question)
        
        # History format karo
        history = self.__formatted_history()

        # Prompt banao
        prompt = self.__prompt.format(
            context = context,
            question = question,
            history = history
        )
        # AI se jawab lo (Groq model response invoke karega)
        # Kyunki ChatGroq complex object return karta hai, isliye .content se clean string nikalenge
        response = self.__llm.invoke(prompt).content

        # History update karo
        self.__chat_history.append({
            "role": "user",
            "content": question
        })
        self.__chat_history.append({
            "role":"assistant",
            "content":response
        })
        return response
    def run(self):
        print("🤖 PDF Chatbot — Powered by RAG + Groq Cloud (Llama 3.1)")
        print("=" * 50)

        # PDF path lo
        pdf_path = input("PDF ka path enter karo: ").strip()

        if not self.load_pdf(pdf_path):
            return 
        
        print("\nCommands: 'quit' to exit.")
        print('-'*50)
        while True:
            question = input("\n👤 You: ").strip()
            
            if not question:
                continue
            elif question.lower() == "quit":
                print("👋 Allah Hafiz!")
                break
            else:
                print("\n🤖 AI: ", end="", flush=True)
                answer = self.ask(question)
                print(answer)
    # Run karo!
if __name__ == "__main__":
    chatbot = PDFChatbot()
    chatbot.run()