from typing import Dict


class Orchestrator:

    CORE_VERSION = "1.0.1"

    def __init__(self):
        self.modules = {}
        self.safe_mode = True

    def register_module(self, name: str, module):
        if name in self.modules:
            raise ValueError(f"Module '{name}' already registered.")
        self.modules[name] = module

    def _validate_payload(self, payload):
        if not isinstance(payload, dict):
            raise TypeError("Payload must be a dictionary.")
        return True

    def execute(self, name: str, payload: Dict) -> Dict:

        if not self.safe_mode:
            raise RuntimeError("System is not in SAFE MODE.")

        if name not in self.modules:
            return {
                "status": "error",
                "engine": name,
                "data": None,
                "error": f"Module '{name}' not found."
            }

        try:
            self._validate_payload(payload)

            module = self.modules[name]
            result = module.run(payload)

            return result

        except Exception as e:
            return {
                "status": "error",
                "engine": name,
                "data": None,
                "error": str(e)
            }

    def enable_safe_mode(self):
        self.safe_mode = True

    def disable_safe_mode(self):
        raise PermissionError("Safe mode cannot be disabled in CORE.")
