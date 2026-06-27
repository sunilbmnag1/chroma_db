import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")

documents = [
    {"id":"doc1", "text":"Hello, World !!"},
    {"id":"doc2", "text":"How are u today ?"},
    {"id":"doc3", "text":"See you later"}
]

for doc in documents:
    # collection.add(doc)
    collection.upsert(ids=doc["id"], documents=[doc["text"]])

query_text = "Hello, World !!"

results = collection.query(
    query_texts=[query_text],
    n_results=3,
)

print(results)

for idx, document in enumerate(results["documents"][0]):
    doc_id = results["ids"][0][idx]
    distance = results["distances"][0][idx]
    print(
        f" For Query: {query_text}, \n Found similar document: {document} (ID: {doc_id}, Distance: {distance})" 
    )