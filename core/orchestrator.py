from core.dna import SystemDNA
from core.logger import Logger
from core.usage_tracker import UsageTracker

from core.engines.image_engine import ImageEngine


class Orchestrator:

    def __init__(self):
        self.dna = SystemDNA()
        self.logger = Logger()
        self.usage = UsageTracker()

        self.engines = {
            "image": ImageEngine()
        }

    def run(self, engine_name, payload):

        auth = self.dna.authorize(engine_name, payload)

        if not auth["allowed"]:
            return auth

        engine = self.engines.get(engine_name)

        if not engine:
            return {
                "status": "error",
                "message": "Engine not found"
            }

        result = engine.execute(payload)

        self.usage.track(engine_name)
        self.logger.log(engine_name, payload)

        return result
