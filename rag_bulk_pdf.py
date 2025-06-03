# Process a large directory of PDFs in batches to manage memory efficiently, creating a FAISS vector store incrementally for scalability.

from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os

# Initialize embeddings
embeddings = OpenAIEmbeddings(openai_api_key="your-openai-api-key")

# Initialize an empty FAISS vector store
vector_store = None

# Process PDFs in batches
directory_path = "./pdfs"
batch_size = 2  # Process 2 PDFs at a time
pdf_files = [f for f in os.listdir(directory_path) if f.endswith(".pdf")]

for i in range(0, len(pdf_files), batch_size):
    batch_files = pdf_files[i:i + batch_size]
    print(f"Processing batch {i // batch_size + 1}: {batch_files}")

    # Load batch of PDFs
    batch_loader = PyPDFDirectoryLoader(
        path=directory_path,
        glob=",".join(batch_files)  # Load only specific files
    )
    documents = batch_loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50,
        length_function=len,
        add_start_index=True
    )
    chunked_documents = text_splitter.split_documents(documents)

    # Create or merge FAISS vector store
    if vector_store is None:
        vector_store = FAISS.from_documents(chunked_documents, embeddings)
    else:
        new_vector_store = FAISS.from_documents(chunked_documents, embeddings)
        vector_store.merge_from(new_vector_store)

# Save the vector store
vector_store.save_local("faiss_index")

# Perform a search
query = "What is deep learning?"
relevant_docs = vector_store.similarity_search(query, k=3)

# Print results
print(f"Found {len(relevant_docs)} relevant documents:")
for i, doc in enumerate(relevant_docs):
    print(f"Document {i + 1}:")
    print(f"Source: {doc.metadata['source']}, Page: {doc.metadata['page']}, Start Index: {doc.metadata['start_index']}")
    print(f"Content: {doc.page_content[:100]}...")
    print("-" * 50)
