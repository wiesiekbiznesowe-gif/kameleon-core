from typing import Dict
from core.guard import Guard


class Orchestrator:

    CORE_VERSION = "1.0.2"

    def __init__(self):
        self.modules = {}
        self.safe_mode = True

    def register_module(self, name: str, module):
        if name in self.modules:
            raise ValueError(f"Module '{name}' already registered.")
        self.modules[name] = module

    def execute(self, name: str, payload: Dict) -> Dict:

        if not self.safe_mode:
            raise RuntimeError("System is not in SAFE MODE.")

        if name not in self.modules:
            return {
                "status": "error",
                "engine": name,
                "version": self.CORE_VERSION,
                "data": None,
                "error": f"Module '{name}' not found."
            }

        try:
            # 🔐 GLOBAL GUARD VALIDATION
            guard_result = Guard.validate(name, payload)

            if not guard_result.get("allowed"):
                return {
                    "status": "blocked",
                    "engine": name,
                    "version": self.CORE_VERSION,
                    "data": None,
                    "error": guard_result.get("error")
                }

            # 🚀 ENGINE EXECUTION
            module = self.modules[name]
            result = module.run(payload)

            return {
                "status": "success",
                "engine": name,
                "version": self.CORE_VERSION,
                "data": result,
                "error": None
            }

        except Exception as e:
            return {
                "status": "error",
                "engine": name,
                "version": self.CORE_VERSION,
                "data": None,
                "error": str(e)
            }

    def enable_safe_mode(self):
        self.safe_mode = True

    def disable_safe_mode(self):
        raise PermissionError("Safe mode cannot be disabled in CORE.")
