from dataclasses import dataclass, field
from typing import List, Dict, Any
import uuid
import time


@dataclass
class ExecutionState:

    execution_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: float = field(default_factory=time.time)

    goal: str = ""

    plan: List[str] = field(default_factory=list)

    retrieved_docs: List[Dict] = field(default_factory=list)

    intermediate_results: Dict[str, Any] = field(default_factory=dict)

    final_answer: str = ""

    status: str = "RUNNING"