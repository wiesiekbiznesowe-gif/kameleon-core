from core.base_engine import BaseEngine


class EchoEngine(BaseEngine):

    def _execute(self, payload: dict):
        text = payload.get("message", "")
        return {
            "echo": text.upper()
        }
