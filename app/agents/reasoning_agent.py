from core.event_log import EventLogger
from llm.router import ModelRouter


class ReasoningAgent:

    def __init__(self):
        self.llm = ModelRouter()
        self.logger = EventLogger()

    def run(self, state):

        question = state.goal
        docs = state.retrieved_docs

        context = "\n\n".join([doc["chunk"] for doc in docs])

        prompt = f"""
                    You are an AI governance assistant.

                    Answer the question using ONLY the provided policy context.

                    If the answer is not present in the context, say:
                    "I could not find this information in the policy documents."

                    Policy Context:
                    {context}

                    Question:
                    {question}

                    Answer in clear sentences using the policy information.
                    """

        
        self.logger.trace(
            state.execution_id,
            "generate_answer",
            "ReasoningAgent",
            "started"
        )
        response = self.llm.generate(prompt)

        state.final_answer = response
        state.intermediate_results["reasoning"] = response
        self.logger.trace(
            state.execution_id,
            "generate_answer",
            "ReasoningAgent",
            "completed",
            {"answer": state.final_answer}
        )
        return state