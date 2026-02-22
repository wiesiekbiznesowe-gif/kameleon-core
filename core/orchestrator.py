from typing import Dict
from core.guard import Guard
from core.logger import CoreLogger


class Orchestrator:

    CORE_VERSION = "1.0.3"

    def __init__(self):
        self.modules = {}
        self.safe_mode = True
        self.logger = CoreLogger.get_logger()

    def register_module(self, name: str, module):
        if name in self.modules:
            raise ValueError(f"Module '{name}' already registered.")
        self.modules[name] = module
        self.logger.info(f"Module registered: {name}")

    def execute(self, name: str, payload: Dict) -> Dict:

        if not self.safe_mode:
            raise RuntimeError("System is not in SAFE MODE.")

        if name not in self.modules:
            self.logger.warning(f"Module not found: {name}")
            return {
                "status": "error",
                "engine": name,
                "version": self.CORE_VERSION,
                "data": None,
                "error": f"Module '{name}' not found."
            }

        try:
            guard_result = Guard.validate(name, payload)

            if not guard_result.get("allowed"):
                self.logger.warning(f"Blocked by guard: {guard_result.get('error')}")
                return {
                    "status": "blocked",
                    "engine": name,
                    "version": self.CORE_VERSION,
                    "data": None,
                    "error": guard_result.get("error")
                }

            module = self.modules[name]
            result = module.run(payload)

            self.logger.info(f"Execution success: {name}")

            return {
                "status": "success",
                "engine": name,
                "version": self.CORE_VERSION,
                "data": result,
                "error": None
            }

        except Exception as e:
            self.logger.error(f"Execution error in {name}: {str(e)}")

            return {
                "status": "error",
                "engine": name,
                "version": self.CORE_VERSION,
                "data": None,
                "error": str(e)
            }

    def enable_safe_mode(self):
        self.safe_mode = True
        self.logger.info("SAFE MODE enabled")

    def disable_safe_mode(self):
        raise PermissionError("Safe mode cannot be disabled in CORE.")
