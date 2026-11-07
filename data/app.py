import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from langchain_ollama import ChatOllama




st.set_page_config(
    page_title="INSURECRM Retention AI Chatbot",
    page_icon="🏥",
    layout="wide"
)




st.title("🏥 INSURECRM – Retention AI Chatbot")
st.write("RAG-based Insurance Assistant")




embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)




client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="insurance_documents"
)




llm = ChatOllama(
    model="llama3.2",
    temperature=0
)




def ask_rag(query, document_type="All Documents"):

    # Convert user question into embedding
    query_embedding = embedding_model.encode(
        query
    ).tolist()


    # -----------------------------------------------------
    # Retrieval without metadata filter
    # -----------------------------------------------------

    if document_type == "All Documents":

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=5
        )


    # -----------------------------------------------------
    # Retrieval with metadata filter
    # -----------------------------------------------------

    else:

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=5,
            where={
                "document_type": document_type
            }
        )


    # Get retrieved document chunks
    retrieved_docs = results["documents"][0]


    # Combine retrieved chunks into context
    context = "\n\n".join(
        retrieved_docs
    )


    # -----------------------------------------------------
    # RAG Prompt
    # -----------------------------------------------------

    prompt = f"""
You are an insurance information assistant.

Answer the question using only the information
provided in the context.

If the answer is not available in the context, say:

"I could not find the answer in the provided documents."

Context:
{context}

Question:
{query}

Answer:
"""


    # Generate answer using Llama 3.2
    response = llm.invoke(
        prompt
    )


    return response.content, results




document_type = st.selectbox(
    "Select Document Type",
    [
        "All Documents",
        "Policy Usage Guide",
        "Brochure",
        "Prospectus / Sales Literature"
    ]
)




question = st.text_input(
    "Ask your insurance-related question:"
)


# =========================================================
# 9. ASK QUESTION BUTTON
# =========================================================

if st.button("Ask Question"):

    if question:

        # Loading message
        with st.spinner(
            "Searching documents and generating answer..."
        ):

            answer, results = ask_rag(
                question,
                document_type
            )


        # =================================================
        # 10. DISPLAY ANSWER
        # =================================================

        st.subheader("Answer")

        st.write(answer)


        # =================================================
        # 11. DISPLAY RETRIEVED SOURCES
        # =================================================

        st.subheader("Retrieved Sources")


        for i, metadata in enumerate(
            results["metadatas"][0]
        ):

            with st.expander(
                f"Source {i+1}: "
                f"{metadata['source']} "
                f"— Page {metadata['page']}"
            ):

                st.write(
                    "**Document Type:**",
                    metadata["document_type"]
                )

                st.write(
                    "**Retrieved Text:**"
                )

                st.write(
                    results["documents"][0][i]
                )


    else:

        st.warning(
            "Please enter a question."
        )