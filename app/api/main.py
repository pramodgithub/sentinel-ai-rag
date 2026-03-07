from fastapi import FastAPI
from app.embedding.embedder import embed_text
from app.storage.vector_store import insert_chunk, search_similar
from app.ingestion.chunker import chunk_text
from app.api.query_schema import QueryRequest

app = FastAPI()

@app.post("/query")
def query_docs(req: QueryRequest):

    query_embedding = embed_text(req.question)

    results = search_similar(query_embedding, req.top_k)

    return {
        "question": req.question,
        "results": results
    }

@app.post("/ingest")
def ingest_document(doc_id: str, text: str):

    chunks = chunk_text(text)

    for chunk in chunks:
        embedding = embed_text(chunk)
        insert_chunk(doc_id, chunk, embedding)

    return {"chunks_ingested": len(chunks)}