from rag import search_documents
from llm import generate_answer


def knowledge_agent(question):

    documents = search_documents(question)

    if not documents:

        return {
            "agent_decision": "No relevant enterprise knowledge found",
            "context": "",
            "sources": [],
            "answer": (
                "The information is not available "
                "in the enterprise knowledge base."
            )
        }

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    answer = generate_answer(
        question,
        context
    )

    sources = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "Unknown document"
        )

        page = document.metadata.get(
            "page",
            None
        )

        if page is not None:

            page = page + 1

            sources.append(
                f"{source} — Page {page}"
            )

        else:

            sources.append(
                source
            )

    return {
        "agent_decision": "Retrieve enterprise knowledge",
        "context": context,
        "sources": sources,
        "answer": answer
    }