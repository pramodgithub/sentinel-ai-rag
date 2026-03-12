from agents.capability_registry import CapabilityRegistry
from tools.log_tool import LogTool
from tools.metrics_tool import MetricsTool
from tools.restart_tool import RestartTool
from tools.monitor_tool import MonitorTool
from tools.close_incident_tool import CloseIncidentTool


class Orchestrator:

    def __init__(self):

        self.registry = CapabilityRegistry()

        self.registry.register("check_logs", LogTool())
        self.registry.register("inspect_metrics", MetricsTool())
        self.registry.register("restart_container", RestartTool())
        self.registry.register("monitor_service", MonitorTool())
        self.registry.register("close_incident", CloseIncidentTool())

    def run(self, state):

        for step in state.plan:

            print(f"Executing step: {step}")

            agent = self.registry.get_agent(step)

            if agent is None:
                raise Exception(f"No agent registered for step: {step}")

            state = agent.run(state)

        return state