
# InsureCRM – RAG-Based Insurance Chatbot

## Project Overview
InsureCRM is a Retrieval-Augmented Generation (RAG) based insurance chatbot designed to answer insurance-related questions using information retrieved from insurance documents.

The application combines document processing, semantic search, vector databases, and Large Language Models (LLMs) to generate context-aware responses.

## Key Features
- PDF document processing
- Text extraction and chunking
- Text embeddings generation
- Vector storage using ChromaDB
- Semantic document retrieval
- Context-based AI responses
- RAG evaluation using RAGAS
- Interactive interface using Streamlit

## Technologies Used
- Python
- Streamlit
- LangChain
- ChromaDB
- Sentence Transformers
- Ollama (Llama 3.2)
- RAGAS

## Project Workflow
1. Load insurance PDF documents.
2. Extract text from the documents.
3. Split text into smaller chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in ChromaDB.
6. Retrieve relevant chunks based on user queries.
7. Generate responses using the Llama 3.2 model.
8. Evaluate response quality using RAGAS.

## Dataset Information
- PDF Documents: 7
- Total Pages: 131
- Total Text Chunks: 872

## Evaluation Results

| Metric | Score |
|---|---:|
| Faithfulness | 1.00 |
| Answer Relevancy | 0.9265 |
| Context Recall | 0.7630 |

Evaluation was performed using RAGAS on 18 cleaned evaluation samples.

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/itzkhushiix2006-ai/InsureCRM-RAG-Insurance-Chatbot.git
```

Navigate to the project directory:

```bash
cd InsureCRM-RAG-Insurance-Chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

Note: Ollama and the Llama 3.2 model must be installed separately. Refer to the Ollama documentation for setup instructions.

## Future Improvements
- Improve document retrieval accuracy.
- Support additional insurance document formats.
- Enhance response quality and context handling.
- Add authentication and conversation history.
- Explore cloud deployment.

## Author
Khushi Singh

B.Tech – Computer Science and Engineering
