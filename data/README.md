
# InsureCRM – RAG-Based Insurance Chatbot

## 1. Project Overview

InsureCRM is a Retrieval-Augmented Generation (RAG) based insurance chatbot prototype designed to retrieve relevant information from health insurance PDF documents and generate context-based responses to user queries.

The project explores document processing, text chunking, embedding generation, vector database storage, information retrieval, and retrieval evaluation.

## 2. Problem Statement

Insurance documents contain detailed policy information that can be difficult and time-consuming to search manually. This project explores how a RAG pipeline can help users retrieve relevant information from insurance documents more efficiently.

## 3. Project Objectives

- Process health insurance PDF documents.
- Extract and clean text from PDF files.
- Split documents into manageable text chunks.
- Generate embeddings for semantic search.
- Store and retrieve document chunks using ChromaDB.
- Experiment with different retrieval strategies.
- Evaluate retrieval performance using Precision, Recall, and F1-score.

## 4. Technologies Used

- Python
- Jupyter Notebook
- PyMuPDF
- LangChain
- Sentence Transformers
- all-MiniLM-L6-v2
- ChromaDB
- Ollama with Llama 3.2 for the local prototype

## 5. Project Workflow

1. Load health insurance PDF documents.
2. Extract text and associated document metadata.
3. Split the extracted text into chunks.
4. Generate vector embeddings using the embedding model.
5. Store embeddings and document chunks in ChromaDB.
6. Retrieve relevant chunks for a user query.
7. Experiment with semantic, BM25, hybrid, and Reciprocal Rank Fusion (RRF) retrieval.
8. Evaluate retrieval results using Precision, Recall, and F1-score.

## 6. Document Processing Configuration

The documented experiments used the following configuration:

- PDF documents: 7
- Total pages: 131
- Document chunks: 872
- Chunk size: 512 characters
- Chunk overlap: 100 characters
- Embedding model: all-MiniLM-L6-v2
- Vector database: ChromaDB

## 7. Retrieval Evaluation

The following results were recorded in the project evaluation report.

| Retrieval Method | Precision | Recall | F1-score |
|---|---:|---:|---:|
| Baseline Semantic | 0.20 | 0.0183 | 0.0336 |
| BM25 | 0.16 | 0.0149 | 0.0272 |
| Hybrid | 0.20 | 0.0183 | 0.0336 |
| Reciprocal Rank Fusion (RRF) | 0.20 | 0.0172 | 0.0317 |
| Top-k = 10 | 0.12 | 0.0218 | 0.0368 |

These are the recorded results from the current evaluation report. The low scores indicate that retrieval quality needs further improvement. Results should be interpreted according to the evaluation dataset and metric implementation.

## 8. Project Structure

```text
02_InsureCRM_RAG_Insurance_Chatbot/
├── InsureCRM_Project/
│   ├── Documentation/
│   ├── Notebooks/
│   ├── Source_Code/
│   ├── Evaluation_Results/
│   └── Screenshots/
├── README.md
└── requirements.txt
```

The internal folder names may differ depending on the existing project files.

## 9. Setup and Execution

### Step 1: Create a Python Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Install and Start Ollama

For the existing local prototype, install Ollama separately and ensure the Llama 3.2 model is available if the notebook uses it.

```bash
ollama pull llama3.2
```

### Step 4: Launch JupyterLab

```bash
jupyter lab
```

Open the relevant project notebook and execute its cells in the required order.

Note: Exact setup steps may vary depending on the notebook and installed package versions.

## 10. Limitations

- Retrieval evaluation scores are low and require improvement.
- Results depend on document quality, chunking, retrieval configuration, and the evaluation dataset.
- Advanced reranking and RAG-specific evaluation require further work if not already implemented.
- The chatbot should not be treated as a substitute for official policy documents or professional insurance advice.

## 11. Future Improvements

- Improve document cleaning and chunking.
- Tune retrieval parameters and top-k values.
- Add reranking to improve relevance.
- Expand evaluation with representative question-answer pairs.
- Add RAGAS or other suitable RAG evaluation methods.
- Improve source citations and response grounding.
- Add a user-friendly interface and error handling.

## 12. Important Notes

- This folder documents the existing InsureCRM prototype.
- Ollama and Llama 3.2 are used for the local prototype described here.
- Install dependencies according to the actual notebook imports.
- Do not include confidential company documents, customer information, passwords, API keys, or environment files in the project package.
