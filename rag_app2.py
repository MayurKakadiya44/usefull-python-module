import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.utils import embedding_functions

# Sample document (replace with your own chunked documents if available)
sample_document = """
This is a sample document. It contains some information about vector databases.
Vector databases are designed to handle high-dimensional data efficiently.
They are useful for tasks like semantic search and recommendation systems.
"""
# Simple chunking (split by sentences for this example)
chunks = [chunk.strip() for chunk in sample_document.split('.') if chunk.strip()]
print("Chunks:", chunks)

# Initialize the embedding model (e.g., all-MiniLM-L6-v2 for lightweight embeddings)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for the chunks
embeddings = embedding_model.encode(chunks, convert_to_tensor=False).tolist()

# Initialize Chroma client (persistent storage to a local directory)
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Create or get a collection (equivalent to a table in Chroma)
collection_name = "sample_collection"
collection = chroma_client.get_or_create_collection(
    name=collection_name,
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
)

# Prepare data for insertion
# Each chunk needs an ID, embedding, and optional metadata
ids = [f"chunk_{i}" for i in range(len(chunks))]
metadatas = [{"text": chunk} for chunk in chunks]  # Store original text as metadata

# Insert chunks into Chroma
collection.add(
    ids=ids,
    embeddings=embeddings,
    metadatas=metadatas
)

# Verify insertion by querying the collection
print(f"Inserted {collection.count()} documents into the collection.")

# Example: Query the vector store for similar chunks
query_text = "What are vector databases?"
query_embedding = embedding_model.encode([query_text]).tolist()[0]
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2  # Return top 2 similar chunks
)

# Print query results
print("\nQuery Results:")
for i, (id, distance, metadata) in enumerate(zip(results['ids'][0], results['distances'][0], results['metadatas'][0])):
    print(f"Result {i+1}: ID={id}, Distance={distance:.4f}, Text={metadata['text']}")
