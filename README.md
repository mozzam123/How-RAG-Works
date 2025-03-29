# Groq RAG Demo

This project demonstrates a simple **Retrieval-Augmented Generation (RAG)** system using the **Groq API**. It simulates retrieving relevant document chunks and generating answers based on the given context.  

## ✨ Features

- Uses **Groq API** for text generation.
- Implements a simple **RAG-style question-answering** system.
- Simulated **document retrieval** from predefined sample text.
- Measures **response time** for API calls.
- Easy-to-follow implementation with **Python and dotenv** for environment variables.

## 📌 Requirements

Ensure you have the following installed:

- Python **3.8+**
- A valid **Groq API Key** (stored in `.env`)
- Required Python packages (see [Installation](#installation))

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/groq-rag-demo.git
   cd groq-rag-demo
  

2. **Set up a virtual environment (recommended)**
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```


3. **Install dependencies**
```bash
  pip install -r requirements.txt
  ```
  

4. **Set up your environment variables**

- Create a .env file in the project root
- Add your Groq API key:
  ```
  GROQ_API_KEY=your_api_key_here
  ```

## 🛠️ Usage

1. **Run the demo script:**
```
python groq_rag_demo.py
```

2. **The script will:**
- Load sample documents as context
- Process a test query ("who is mozzam and what does he do? he lives where?")
- Display the context, generated response, and performance metrics


## 🔧 Customization
- **Change the test query:** Modify the query variable in ```test_groq_rag()```
- **Update sample documents:** Edit the ```sample_documents```
- **Try different models:** Change ```model="llama3-70b-8192"``` to other Groq-supported models
- **Adjust generation parameters:** Modify ```temperature``` or ```max_tokens``` in the API call

## 📊 Sample Output

You should see output similar to:
```
Testing Groq API with query: 'who is mozzam and what does he do? he lives where?'
Context provided: ----------------------------------------
[Your sample documents will be displayed here]
----------------------------------------

Groq API Response: ----------------------------------------
Mozzam is a software engineer who worked at Tubelight communications platform. He lives in Mumbai, India, and is 11 years old.
----------------------------------------
Response time: 0.87 seconds
Model used: llama3-70b-8192
Total tokens: 342
```

