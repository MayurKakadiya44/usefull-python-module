
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.vectorstores import FAISS
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings  # Or use OllamaEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Specify the directory containing PDF files
directory_path = "./pdfs"

# Initialize the loader
loader = PyPDFDirectoryLoader(path=directory_path)

# Load all PDFs into a list of Document objects
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50, length_function=len, 
    separators=["\n\n", "\n", " ", ""],
    add_start_index=True  # Enable start_index in metadata
)

# Create documents (chunks with metadata)
chunked_documents = text_splitter.create_documents([documents])

# Initialize embeddings (replace with OllamaEmbeddings for local models)
embeddings = OpenAIEmbeddings(openai_api_key="your-openai-api-key")  # Set your API key
# embeddings = OllamaEmbeddings(model="llama3")
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create a FAISS vector store from the chunked documents
vector_store = FAISS.from_documents(chunked_documents, embeddings)
# Initialize Chroma vector store
# vector_store = Chroma.from_texts(
#    texts=chunks,
#    embedding=embedding_model,
#    ids=ids,
#    metadatas=metadatas,
#    persist_directory="./chroma_db"
#)

# Initialize the LLM (e.g., OpenAI with temperature=0.5 from your earlier question)
llm = ChatOpenAI(model_name="gpt-4", temperature=0.5, openai_api_key="your-openai-api-key")

# Create a RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # Simple method to combine retrieved documents
    retriever=vector_store.as_retriever(search_kwargs={"k": 3}),  # Retrieve top 3 chunks
    return_source_documents=True  # Return source metadata
)

# Query the RAG system
query = "What are the applications of AI?"
result = qa_chain({"query": query})

# Print the answer and source documents
print("Answer:", result["result"])
print("\nSource Documents:")
for doc in result["source_documents"]:
    print(f"  Source: {doc.metadata['source']}, Page: {doc.metadata['page']}, Start Index: {doc.metadata['start_index']}")
    print(f"  Content: {doc.page_content[:100]}...")
    print("-" * 50)
