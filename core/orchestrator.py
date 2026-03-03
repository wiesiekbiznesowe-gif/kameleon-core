from core.usage_tracker import UsageTracker


class Orchestrator:
    """
    Central execution router for Kameleon Core.
    Responsible for:
    - module registration
    - execution routing
    - usage control layer
    """

    def __init__(self):
        self.modules = {}
        self.usage_tracker = UsageTracker()

    def register_module(self, name: str, module):
        self.modules[name] = module

    def execute(self, module_name: str, payload: dict) -> dict:
        # Check if module exists
        if module_name not in self.modules:
            return {
                "status": "error",
                "message": f"Module '{module_name}' not found"
            }

        # Usage control BEFORE execution
        usage_check = self.usage_tracker.check_and_track(module_name)

        if not usage_check["allowed"]:
            return {
                "status": "blocked",
                "reason": usage_check["reason"]
            }

        module = self.modules[module_name]

        try:
            result = module.execute(payload)
            return result

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
