from core.guard import Guard


class Orchestrator:

    def __init__(self):
        self.modules = {}
        self.safe_mode = True

    def register_module(self, name: str, module):
        if name in self.modules:
            raise ValueError(f"Module '{name}' already registered.")
        self.modules[name] = module

    def execute(self, name: str, payload: dict) -> dict:

        if not self.safe_mode:
            raise RuntimeError("System is not in SAFE MODE.")

        if name not in self.modules:
            return {
                "status": "error",
                "engine": name,
                "data": None,
                "error": f"Module '{name}' not found."
            }

        # 🔒 GLOBAL INPUT GUARD
        validation = Guard.validate(name, payload)

        if not validation.get("allowed"):
            return {
                "status": "error",
                "engine": name,
                "data": None,
                "error": validation.get("error")
            }

        module = self.modules[name]
        return module.run(payload)

    def enable_safe_mode(self):
        self.safe_mode = True

    def disable_safe_mode(self):
        raise PermissionError("Safe mode cannot be disabled in CORE.")
