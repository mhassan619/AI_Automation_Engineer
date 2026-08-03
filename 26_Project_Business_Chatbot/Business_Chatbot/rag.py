from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings # CHANGED FROM OLLAMA
import os

class RAGSystem:
    def __init__(self):
        # Local HuggingFace Embeddings (Fast & Lightweight)
        self.__embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.__vectorstore = None
    
    def load_documents(self, docs_folder="docs"):
        all_docs = []
        
        if not os.path.exists(docs_folder):
            print(f"❌ Folder '{docs_folder}' nahi mila!")
            return False

        for filename in os.listdir(docs_folder):
            filepath = os.path.join(docs_folder, filename)
            
            try:
                loader = TextLoader(filepath, encoding="utf-8")
                docs = loader.load()
                all_docs.extend(docs)
                print(f"✅ Loaded: {filename}")
            except Exception as e:
                print(f"❌ Error loading {filename}: {e}")
        
        if not all_docs:
            return False
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=30
        )
        chunks = splitter.split_documents(all_docs)
        
        self.__vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.__embeddings,
            persist_directory="./chroma_business"
        )
        
        print(f"✅ {len(chunks)} chunks indexed!")
        return True
    
    def get_context(self, question, k=3):
        if not self.__vectorstore:
            # Persistent directory se load karne ki koshish karein
            if os.path.exists("./chroma_business"):
                self.__vectorstore = Chroma(
                    persist_directory="./chroma_business", 
                    embedding_function=self.__embeddings
                )
            else:
                return ""
        
        docs = self.__vectorstore.similarity_search(question, k=k)
        return "\n".join([d.page_content for d in docs])