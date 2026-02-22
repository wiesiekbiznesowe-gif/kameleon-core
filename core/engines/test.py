from core.base_engine import BaseEngine

class Engine(BaseEngine):

    def _execute(self, payload: dict):
        text = payload.get("message", "")
        return {
            "test_echo": f"Test engine received: {text}"
        }
