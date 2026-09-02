from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)


def load_documents(folder="data/documents"):

    documents = []

    folder_path = Path(folder)

    if not folder_path.exists():
        raise ValueError(
            f"Folder not found: {folder}"
        )

    for file in folder_path.iterdir():

        if file.suffix.lower() == ".pdf":

            loader = PyPDFLoader(
                str(file)
            )

            documents.extend(
                loader.load()
            )

        elif file.suffix.lower() == ".txt":

            loader = TextLoader(
                str(file),
                encoding="utf-8"
            )

            documents.extend(
                loader.load()
            )

    return documents