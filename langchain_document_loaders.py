from langchain.document_loaders import PyPDFDirectoryLoader

# Specify the directory containing PDF files
directory_path = "./pdfs"

# Initialize the loader
loader = PyPDFDirectoryLoader(path=directory_path)

# Load all PDFs into a list of Document objects
documents = loader.load()

# Print the loaded documents
print(f"Loaded {len(documents)} documents:")
for i, doc in enumerate(documents):
    print(f"Document {i + 1}:")
    print(f"  Source: {doc.metadata['source']}")
    print(f"  Page: {doc.metadata['page']}")
    print(f"  Content (first 100 characters): {doc.page_content[:100]}...")
    print("-" * 50)

Output :
Output (assuming 2 PDFs with 2 and 3 pages):
  
Loaded 5 documents:
Document 1:
  Source: pdfs/ai_intro.pdf
  Page: 0
  Content (first 100 characters): Artificial Intelligence (AI) is the simulation of human intelligence in machines...
Document 2:
  Source: pdfs/ai_intro.pdf
  Page: 1
  Content (first 100 characters): AI involves techniques like machine learning and neural networks...
Document 3:
  Source: pdfs/ai_applications.pdf
  Page: 0
  Content (first 100 characters): AI applications span multiple industries, including healthcare...




