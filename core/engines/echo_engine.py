from core.base_engine import BaseEngine

class EchoEngine(BaseEngine):

    def run(self, payload: dict) -> dict:
        text = payload.get("message", "")
        return {
            "status": "success",
            "echo": text.upper()
        }
