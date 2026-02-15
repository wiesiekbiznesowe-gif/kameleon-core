from core.base_engine import BaseEngine


class Engine(BaseEngine):

    def run(self, payload: dict) -> dict:
        return {
            "status": "success",
            "received": payload
        }
