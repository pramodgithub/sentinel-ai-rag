class CapabilityRegistry:

    def __init__(self):
        self.registry = {}

    def register(self, capability_name, agent):
        self.registry[capability_name] = agent

    def get_agent(self, capability_name):
        return self.registry.get(capability_name)