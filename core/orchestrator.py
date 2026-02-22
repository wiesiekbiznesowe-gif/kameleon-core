from typing import Dict
from core.guard import Guard
from core.logger import CoreLogger
import uuid
import time


class Orchestrator:

    CORE_VERSION = "1.1.0"

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

        execution_id = str(uuid.uuid4())
        start_time = time.time()

        if not self.safe_mode:
            raise RuntimeError("System is not in SAFE MODE.")

        if name not in self.modules:
            self.logger.warning(f"[{execution_id}] Module not found: {name}")
            return {
                "execution_id": execution_id,
                "status": "error",
                "engine": name,
                "version": self.CORE_VERSION,
                "duration_ms": 0,
                "data": None,
                "error": f"Module '{name}' not found."
            }

        try:
            # GLOBAL GUARD VALIDATION
            guard_result = Guard.validate(name, payload)

            if not guard_result.get("allowed"):
                duration = int((time.time() - start_time) * 1000)

                self.logger.warning(
                    f"[{execution_id}] Blocked by guard: {guard_result.get('error')}"
                )

                return {
                    "execution_id": execution_id,
                    "status": "blocked",
                    "engine": name,
                    "version": self.CORE_VERSION,
                    "duration_ms": duration,
                    "data": None,
                    "error": guard_result.get("error")
                }

            # ENGINE EXECUTION
            module = self.modules[name]
            result = module.run(payload)

            duration = int((time.time() - start_time) * 1000)

            self.logger.info(
                f"[{execution_id}] Execution success: {name} ({duration} ms)"
            )

            return {
                "execution_id": execution_id,
                "status": "success",
                "engine": name,
                "version": self.CORE_VERSION,
                "duration_ms": duration,
                "data": result,
                "error": None
            }

        except Exception as e:
            duration = int((time.time() - start_time) * 1000)

            self.logger.error(
                f"[{execution_id}] Execution error in {name}: {str(e)}"
            )

            return {
                "execution_id": execution_id,
                "status": "error",
                "engine": name,
                "version": self.CORE_VERSION,
                "duration_ms": duration,
                "data": None,
                "error": str(e)
            }

    def enable_safe_mode(self):
        self.safe_mode = True
        self.logger.info("SAFE MODE enabled")

    def disable_safe_mode(self):
        raise PermissionError("Safe mode cannot be disabled in CORE.")
