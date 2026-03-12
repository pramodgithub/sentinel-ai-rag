
from sqlalchemy import text
from db.db import engine
from core.event_log import EventLogger
from core.embedding_model import model


class RetrieverAgent:

    def __init__(self):
        self.model = model
        self.logger = EventLogger()

    def run(self, state):

        question = state.goal
        
        self.logger.trace(
            state.execution_id,
            "retrieve_policy_documents",
            "RetrieverAgent",
            "started",
            {"goal": state.goal}
        )

        # Create embedding
        embedding = self.model.encode(question).tolist()

        query = text("""
        SELECT chunk, embedding <-> CAST(:embedding AS vector) AS distance
        FROM document_chunks
        ORDER BY embedding <-> CAST(:embedding AS vector)
        LIMIT 5
        """)

        with engine.connect() as conn:
            results = conn.execute(query, {"embedding": embedding}).fetchall()

        docs = []

        for row in results:
            docs.append({
                "chunk": row[0],
                "distance": row[1]
            })

        state.retrieved_docs = docs
        
        self.logger.trace(
            state.execution_id,
            "retrieve_policy_documents",
            "RetrieverAgent",
            "completed",
            {"docs_found": len(state.retrieved_docs)}
        )
        

        return state