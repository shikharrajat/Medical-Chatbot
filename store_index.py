from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import Pinecone  as PC
from langchain_pinecone import PineconeVectorStore
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

os.environ['PINECONE_API_KEY'] = 'PINECONE_API'
index_name = 'medi-chat'

docsearch = PineconeVectorStore.from_texts(
    [t.page_content for t in text_chunks], 
    embeddings, 
    index_name=index_name
)