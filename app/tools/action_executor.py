class ActionExecutor:

    def __init__(self, registry, logger):
        self.registry = registry
        self.logger = logger

    def run(self, state):

        for step in state.plan:

            tool = self.registry.get(step)

            if not tool:
                continue

            self.logger.log(
                state.execution_id,
                "ACTION_STARTED",
                {
                    "step": step,
                    "incident_id": state.incident_id
                }
            )

            result = tool.execute(state)

            state.intermediate_results[step] = result

            self.logger.log(
                state.execution_id,
                "ACTION_COMPLETED",
                {
                    "step": step,
                    "result": result
                }
            )

        return state