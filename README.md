ChromaDB Basic Demo

A simple Python project demonstrating how to use Chroma to create a collection, insert documents, and perform similarity search.

Project Overview

This project shows how to:

* Create an in-memory ChromaDB client
* Create a collection
* Insert or update documents using upsert()
* Query similar documents using text
* Retrieve IDs and distances for matched documents

⸻

Project Structure

chroma_db/
│── app.py
│── venv/
│── README.md

⸻

Prerequisites

* Python 3.10+
* Virtual Environment (venv)

⸻

Setup Instructions

1. Clone the repository

git clone https://github.com/sunilbmnag1/chroma_db.git
cd chroma_db

2. Create virtual environment (if not already created)

python3 -m venv venv

3. Activate virtual environment
Mac/Linux

source venv/bin/activate

Windows

venv\Scripts\activate

4. Install dependencies

pip install chromadb

⸻

Running the Project

Execute:

python app.py

⸻

Code Explanation

Create Chroma client

import chromadb
chroma_client = chromadb.Client()

Initializes a ChromaDB client.

⸻

Create collection

collection = chroma_client.create_collection(name="my_collection")

Creates a new collection named my_collection.

⸻

Add documents

Documents are inserted using:

collection.upsert(ids=doc["id"], documents=[doc["text"]])

This will insert new documents or update existing ones.

⸻

Query documents

results = collection.query(
    query_texts=[query_text],
    n_results=3,
)

This finds the top 3 most similar documents.

⸻

Example Output

For Query: Hello, World !!
Found similar document: Hello, World !! (ID: doc1, Distance: 0.0)
Found similar document: How are u today ? (ID: doc2, Distance: ...)

⸻

Notes

* This example uses in-memory storage, so data will not persist after the program ends.
* To persist data, use PersistentClient.

Example:

chroma_client = chromadb.PersistentClient(path="./chroma_storage")

⸻

Future Improvements

* Add persistent storage
* Store embeddings explicitly
* Build a semantic search API
* Integrate with LangChain

⸻
