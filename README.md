\# 🤖 Enterprise Knowledge Assistant



An AI-powered Enterprise Knowledge Assistant built using \*\*Retrieval-Augmented Generation (RAG)\*\* and \*\*AI Agents\*\*.



\## 🚀 Features



\* 📄 PDF and TXT document upload

\* ✂️ Automatic document chunking

\* 🧠 HuggingFace sentence embeddings

\* 🗄️ Chroma vector database

\* 🔍 Semantic document retrieval

\* 🤖 AI Agent for knowledge retrieval

\* ✨ FLAN-T5 answer generation

\* 📖 Source/page information

\* 💬 Conversational chat history

\* 📊 Knowledge-base dashboard

\* 🔄 Automatic vector database rebuilding



\## 🏗️ Architecture



```text

User Question

&#x20;     ↓

&#x20;  AI Agent

&#x20;     ↓

Vector Database

&#x20;     ↓

Semantic Retrieval

&#x20;     ↓

Relevant Document Chunks

&#x20;     ↓

&#x20;  FLAN-T5

&#x20;     ↓

Generated Answer

&#x20;     ↓

Source Information

```



\## 📁 Project Structure



```text

Enterprise-Knowledge-Assistant/

│

├── app/

│   ├── \_\_init\_\_.py

│   ├── main.py

│   ├── rag.py

│   ├── agent.py

│   ├── document\_loader.py

│   └── llm.py

│

├── data/

│   └── documents/

│

├── vectorstore/

│

├── .github/

│   └── workflows/

│       └── python.yml

│

├── requirements.txt

├── README.md

└── .gitignore

```



\## 🛠️ Technologies



\* Python

\* Streamlit

\* LangChain

\* ChromaDB

\* HuggingFace Transformers

\* Sentence Transformers

\* PyPDF

\* Retrieval-Augmented Generation

\* AI Agents



\## ▶️ Installation



Clone the repository and enter the project directory.



```bash

pip install -r requirements.txt

```



\## ▶️ Run the Application



```bash

streamlit run app/main.py

```



\## 📚 Usage



1\. Open the Streamlit application.

2\. Upload a PDF or TXT enterprise document.

3\. Click \*\*Build Knowledge Base\*\*.

4\. Enter a question.

5\. The AI Agent retrieves relevant information.

6\. FLAN-T5 generates the answer.

7\. The application displays the retrieved sources.



\## 🔍 RAG Pipeline



```text

Documents

&#x20;   ↓

Text Extraction

&#x20;   ↓

Text Chunking

&#x20;   ↓

Embeddings

&#x20;   ↓

Chroma Vector Database

&#x20;   ↓

Semantic Search

&#x20;   ↓

AI Agent

&#x20;   ↓

FLAN-T5

&#x20;   ↓

Answer + Sources

```



\## 🎯 Project Objective



The objective of this project is to provide an intelligent enterprise knowledge system that allows users to ask natural-language questions about organizational documents and receive answers based on retrieved enterprise information.



\## 👨‍💻 Project Status



Core RAG functionality implemented successfully.



Future improvements can include authentication, document management, advanced agent workflows, conversation persistence, and cloud deployment.



