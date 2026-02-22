from core.base_engine import BaseEngine

class EchoEngine(BaseEngine):

    def run(self, payload: dict) -> dict:
        try:
            text = payload.get("message", "")

            return {
                "status": "success",
                "engine": "echo",
                "data": {
                    "echo": text.upper()
                },
                "error": None
            }

        except Exception as e:
            return {
                "status": "error",
                "engine": "echo",
                "data": None,
                "error": str(e)
            }
