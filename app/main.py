import os

import streamlit as st

from rag import create_vector_database
from agent import knowledge_agent


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)


# ==========================================================
# SESSION STATE
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "knowledge_base_ready" not in st.session_state:
    st.session_state.knowledge_base_ready = False


# ==========================================================
# HEADER
# ==========================================================

st.title("🤖 Enterprise Knowledge Assistant")

st.write(
    "AI-powered Enterprise Knowledge Assistant using "
    "Retrieval-Augmented Generation (RAG) and AI Agents."
)


# ==========================================================
# DASHBOARD
# ==========================================================

documents_folder = "data/documents"

if os.path.exists(documents_folder):

    document_count = len(
        [
            file
            for file in os.listdir(documents_folder)
            if file.lower().endswith((".pdf", ".txt"))
        ]
    )

else:

    document_count = 0


chat_count = len(
    st.session_state.messages
) // 2


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "📄 Documents",
        document_count
    )


with col2:

    st.metric(
        "💬 Questions",
        chat_count
    )


with col3:

    status = (
        "Ready"
        if st.session_state.knowledge_base_ready
        else "Not Built"
    )

    st.metric(
        "🧠 RAG Status",
        status
    )


with col4:

    st.metric(
        "🔍 Retrieval",
        "Top 3"
    )


st.markdown("---")


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.header("📚 Knowledge Base")

st.sidebar.write(
    "Upload enterprise documents and create "
    "a searchable knowledge base."
)


uploaded_file = st.sidebar.file_uploader(
    "Upload PDF or TXT",
    type=["pdf", "txt"]
)


if uploaded_file is not None:

    documents_folder = "data/documents"

    os.makedirs(
        documents_folder,
        exist_ok=True
    )

    file_path = os.path.join(
        documents_folder,
        uploaded_file.name
    )

    with open(file_path, "wb") as file:

        file.write(
            uploaded_file.getbuffer()
        )

    st.sidebar.success(
        f"Uploaded: {uploaded_file.name}"
    )


# ==========================================================
# BUILD KNOWLEDGE BASE
# ==========================================================

if st.sidebar.button(
    "🔄 Build Knowledge Base"
):

    with st.spinner(
        "Processing documents and creating embeddings..."
    ):

        try:

            create_vector_database()

            st.session_state.knowledge_base_ready = True

            st.sidebar.success(
                "Knowledge base created successfully!"
            )

            st.rerun()

        except Exception as e:

            st.sidebar.error(
                f"Error: {e}"
            )


# ==========================================================
# CLEAR CHAT
# ==========================================================

if st.sidebar.button(
    "🗑️ Clear Chat"
):

    st.session_state.messages = []

    st.rerun()


# ==========================================================
# RAG ARCHITECTURE
# ==========================================================

st.sidebar.markdown("---")

st.sidebar.subheader(
    "🔍 RAG Architecture"
)

st.sidebar.write(
    "📄 Documents"
)

st.sidebar.write("↓")

st.sidebar.write(
    "✂️ Text Chunking"
)

st.sidebar.write("↓")

st.sidebar.write(
    "🧠 Embeddings"
)

st.sidebar.write("↓")

st.sidebar.write(
    "🗄️ Chroma Vector DB"
)

st.sidebar.write("↓")

st.sidebar.write(
    "🤖 AI Agent"
)

st.sidebar.write("↓")

st.sidebar.write(
    "✨ FLAN-T5"
)

st.sidebar.write("↓")

st.sidebar.write(
    "💬 Answer"
)


# ==========================================================
# MAIN CHAT
# ==========================================================

st.subheader(
    "💬 Ask the Enterprise Assistant"
)


# Display chat history

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


# ==========================================================
# CHAT INPUT
# ==========================================================

question = st.chat_input(
    "Ask a question about your enterprise documents..."
)


if question:

    # ------------------------------------------------------
    # USER MESSAGE
    # ------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    with st.chat_message("user"):

        st.write(question)


    # ------------------------------------------------------
    # ASSISTANT
    # ------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "Searching enterprise knowledge..."
        ):

            try:

                result = knowledge_agent(
                    question
                )


                # Agent decision

                st.info(
                    "🤖 Agent Decision: "
                    + result["agent_decision"]
                )


                # Answer

                st.subheader(
                    "✅ AI Answer"
                )

                st.write(
                    result["answer"]
                )


                # Sources

                if result.get("sources"):

                    st.subheader(
                        "📖 Sources"
                    )

                    unique_sources = list(
                        dict.fromkeys(
                            result["sources"]
                        )
                    )

                    for source in unique_sources:

                        st.write(
                            f"📄 {source}"
                        )


                # Retrieved knowledge

                if result.get("context"):

                    with st.expander(
                        "📚 View Retrieved Knowledge"
                    ):

                        st.write(
                            result["context"]
                        )


                # Save response

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": result["answer"]
                    }
                )


            except Exception as e:

                st.error(
                    f"Error: {e}"
                )