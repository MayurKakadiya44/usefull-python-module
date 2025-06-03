from langchain.text_splitter import RecursiveCharacterTextSplitter

# Sample text
text = """Introduction
This is a sample document about artificial intelligence. It explores the basics of AI and its applications.

What is AI?
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines. Machines are programmed to think and learn like humans, performing tasks such as problem-solving, decision-making, and pattern recognition.

Applications of AI
AI is used in various fields:
- Healthcare: AI helps in diagnosing diseases and personalizing treatments.
- Finance: AI detects fraud and automates trading.
- Autonomous Vehicles: AI enables self-driving cars to navigate roads safely.

Conclusion
AI is transforming industries and will continue to evolve, bringing new opportunities and challenges."""

# Initialize the text splitter with add_start_index=True
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50,
    length_function=len,
    separators=["\n\n", "\n", " ", ""],
    add_start_index=True  # Enable start_index in metadata
)

# Create documents (chunks with metadata)
documents = text_splitter.create_documents([text])

# Print chunks with start_index from metadata
for i, doc in enumerate(documents):
    print(f"Document {i + 1}:")
    print(f"Content: {doc.page_content}")
    print(f"Start Index: {doc.metadata['start_index']}")
    print(f"Metadata: {doc.metadata}\n")


Output :

Document 1:
Content: Introduction
This is a sample document about artificial intelligence. It explores the basics of AI and its applications.
Start Index: 0
Metadata: {'start_index': 0}

Document 2:
Content: What is AI?
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines. Machines are programmed to think and learn like humans, performing tasks such as problem-solving, decision-making, and pattern recognition.
Start Index: 104
Metadata: {'start_index': 104}

Document 3:
Content: Applications of AI
AI is used in various fields:
- Healthcare: AI helps in diagnosing diseases and personalizing treatments.
- Finance: AI detects fraud and automates trading.
- Autonomous Vehicles: AI enables self-driving cars to navigate roads safely.

Conclusion
AI is transforming industries and will continue to evolve, bringing new opportunities and challenges.
Start Index: 302
Metadata: {'start_index': 302}
