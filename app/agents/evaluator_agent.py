from core.event_log import EventLogger
from llm.router import ModelRouter
import json

class EvaluatorAgent:

    def __init__(self):
        self.llm = ModelRouter()
        self.logger = EventLogger()

    def run(self, state):

        prompt = f"""
                    You are an AI governance evaluator.

            Question:
            {state.goal}

            Retrieved Policy Documents:
            {state.retrieved_docs}

            Generated Answer:
            {state.final_answer}

            Determine:
            1. Is the answer grounded in the documents?
            2. Confidence score (0-1)
            3. If there are issues, list them.
            4. Provide a brief explanation of your evaluation.


            Return JSON:
            {{
                "grounded": true/false,
                "confidence": number,
                "issues": [],
                "explanation": ""
            }}
        """
        self.logger.trace(
            state.execution_id,
            "evaluate_answer",
            "EvaluatorAgent",
            "started"
        )
        evaluation = self.llm.generate(prompt)

        self.logger.trace(
            state.execution_id,
            "evaluate_answer",
            "EvaluatorAgent",
            "completed",
            json.loads(evaluation)
        )
        state.intermediate_results["evaluation"] = evaluation

        return state