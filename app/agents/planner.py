from core.state import ExecutionState
from core.event_log import EventLogger
from llm.router import ModelRouter
import json

class PlannerAgent:

    def __init__(self):
        self.llm = ModelRouter()
        self.logger = EventLogger()

    def run(self, state: ExecutionState):

        self.logger.trace(
            state.execution_id,
            "Planner",
            "PlannerAgent",
            "started",
            {"goal": state.goal}
        )
        prompt = f"""
                You are an incident response planner.

                Incident:
                {incident}

                Diagnosis:
                {diagnosis}

                Create a remediation plan.

                Available actions:
                - check_logs
                - inspect_metrics
                - restart_container
                - monitor_service
                - close_incident

                Return ONLY JSON:

                {
                "plan": ["step1","step2","step3"]
                }
                """

        response = self.llm.generate(prompt)

        plan = json.loads(response)["plan"]
        state.plan = plan

        self.logger.trace(
            state.execution_id,
            "Planner",
            "PlannerAgent",
            "completed",
            {"plan": plan}
        )

        return state