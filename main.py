import groq
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Replace with your valid Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Sample document chunks that would normally come from your vector database
sample_documents = [
    "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to human or animal intelligence. AI research has been defined as the field of study of intelligent agents, which refers to any system that perceives its environment and takes actions that maximize its chance of achieving its goals.",
    "Machine learning (ML) is a subset of AI that focuses on the development of algorithms that can access data and use it to learn for themselves. The primary aim is to allow the computers to learn automatically without human intervention or assistance and adjust actions accordingly.",
    "Large Language Models (LLMs) are a type of machine learning model that can process and generate natural language. They are trained on vast amounts of text data and can perform tasks like translation, summarization, and question answering.",
    "Mozzam is a sofware engineer who was in Tubelight communications platform",
    "mozzam lives in mumbai which is in India",
    "mozzam is 11 years old",
]


def test_groq_rag():
    # Initialize Groq client
    client = groq.Client(api_key=GROQ_API_KEY)

    # Simulated user query
    query = "who is mozzam and what does he do? he lives where?"

    # Join document chunks to create context (in a real RAG system, you'd retrieve relevant documents)
    context = "\n\n".join(sample_documents)

    # Create a RAG-style prompt
    prompt = f"""You are a helpful assistant answering questions based on the provided context.
    
Context:
{context}

Question: {query}

Answer the question based on the context provided."""

    print(f"Testing Groq API with query: '{query}'")
    print("Context provided:", "-" * 40)
    print(context)
    print("-" * 40)

    # Measure response time
    start_time = time.time()

    # Generate response using Groq
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            model="llama3-70b-8192",  # You can change this to any Groq model you want to test
            temperature=0.2,
            max_tokens=500,
        )

        response = chat_completion.choices[0].message.content
        end_time = time.time()

        # Print results
        print("\nGroq API Response:", "-" * 40)
        print(response)
        print("-" * 40)
        print(f"Response time: {end_time - start_time:.2f} seconds")
        print(f"Model used: {chat_completion.model}")
        print(f"Total tokens: {chat_completion.usage.total_tokens}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_groq_rag()
