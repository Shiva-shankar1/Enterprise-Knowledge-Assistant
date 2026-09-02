import shutil
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from document_loader import load_documents


VECTOR_DB = "vectorstore"


def get_embeddings():

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def create_vector_database():

    # Remove old vector database
    vector_path = Path(VECTOR_DB)

    if vector_path.exists():

        shutil.rmtree(vector_path)

    # Load documents
    documents = load_documents()

    if not documents:

        raise ValueError(
            "No documents found in data/documents"
        )

    # Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(
        documents
    )

    # Create embeddings
    embeddings = get_embeddings()

    # Create new vector database
    database = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB
    )

    return database


def load_vector_database():

    if not Path(VECTOR_DB).exists():

        raise ValueError(
            "Knowledge base does not exist. "
            "Click Build Knowledge Base first."
        )

    embeddings = get_embeddings()

    database = Chroma(
        persist_directory=VECTOR_DB,
        embedding_function=embeddings
    )

    return database


def search_documents(question):

    database = load_vector_database()

    results = database.similarity_search(
        question,
        k=3
    )

    return results