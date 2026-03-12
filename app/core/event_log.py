import time


class EventLogger:

    def __init__(self):
        self.events = []

    def log(self, execution_id, event_type, payload=None):

        event = {
            "execution_id": execution_id,
            "event_type": event_type,
            "timestamp": time.time(),
            "payload": payload
        }

        self.events.append(event)
        print(f"[{event_type}] | {payload}", flush=True)

        return event


    def trace(self, execution_id, step, agent, status, payload=None):

        event_type = f"{agent}_{status}".upper()

        payload = payload or {}
        payload["step"] = step
        payload["agent"] = agent
        payload["status"] = status

        return self.log(execution_id, event_type, payload)