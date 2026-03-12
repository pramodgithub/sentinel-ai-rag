from agents.planner import PlannerAgent
from agents.orchestrator import Orchestrator
from core.state import ExecutionState

state = ExecutionState(
    goal="What is AI governance?"
)

planner = PlannerAgent()
orchestrator = Orchestrator()

state = planner.run(state)

state = orchestrator.run(state)

print("\nPlan:")
print(state.plan)

print("\nRetrieved Docs:")
print(state.retrieved_docs)


print("\nEvaluation:")
print(state.intermediate_results["evaluation"])

print("\nFinal Answer:")
print(state.final_answer)