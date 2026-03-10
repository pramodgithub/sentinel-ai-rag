from core.state import ExecutionState
from agents.planner import PlannerAgent

state = ExecutionState(
    goal="What are the carry forward leave rules?"
)

planner = PlannerAgent()

state = planner.run(state)

print(state.plan)