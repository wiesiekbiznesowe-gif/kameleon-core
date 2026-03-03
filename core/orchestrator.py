from core.usage_tracker import UsageTracker
from core.dna import SystemDNA


class Orchestrator:
    """
    Central execution router for Kameleon Core.
    Execution order:
    1. DNA validation
    2. Usage control
    3. Engine execution
    """

    def __init__(self):
        self.modules = {}
        self.usage_tracker = UsageTracker()
        self.dna = SystemDNA()

    def register_module(self, name: str, module):
        self.modules[name] = module

    def execute(self, module_name: str, payload: dict) -> dict:

        # Module existence check
        if module_name not in self.modules:
            return {
                "status": "error",
                "message": f"Module '{module_name}' not found"
            }

        # 🔐 DNA LAYER (FIRST)
        dna_check = self.dna.validate(module_name, payload)

        if not dna_check["allowed"]:
            return {
                "status": "blocked_by_dna",
                "reason": dna_check["reason"]
            }

        # 📊 Usage Control (SECOND)
        usage_check = self.usage_tracker.check_and_track(module_name)

        if not usage_check["allowed"]:
            return {
                "status": "blocked_by_usage",
                "reason": usage_check["reason"]
            }

        # 🚀 Engine Execution (THIRD)
        module = self.modules[module_name]

        try:
            result = module.execute(payload)
            return result

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
