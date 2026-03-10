import requests
from .base_llm import BaseLLM
from .ollama_config import OLLAMA_CONFIG, LLM_MODE

class OllamaLLM(BaseLLM):

    def __init__(self, mode: str = LLM_MODE):
        self.mode = mode
        self.config = OLLAMA_CONFIG[mode]
        self.base_url = self.config["base_url"]
        self.model = self.config["model"]

        # Only cloud needs auth header
        self.headers = {"Content-Type": "application/json"}
        if self.mode == "cloud":
            api_key = self.config.get("api_key")
            if not api_key:
                raise ValueError("OLLAMA_API_KEY is not set for cloud mode")
            self.headers["Authorization"] = f"Bearer {api_key}"


    def generate(self, prompt: str):

        response = requests.post(
            f"{self.base_url}/api/generate",
            headers=self.headers,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False         # set True if you want streaming
            }
        )
        response.raise_for_status()     # raises error on bad status codes
        return response.json()["response"]