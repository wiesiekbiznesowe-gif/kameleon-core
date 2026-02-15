"""
Kameleon Core Orchestrator
Bezpieczny, lokalny koordynator modułów.
Zero połączeń zewnętrznych.
"""

from typing import Dict, Any


class Orchestrator:
    def __init__(self):
        self.modules = {}
        self.safe_mode = True

    def register_module(self, name: str, module: Any) -> None:
        if name in self.modules:
            raise ValueError(f"Module '{name}' already registered.")
        self.modules[name] = module

    def execute(self, name: str, payload: Dict) -> Dict:
        if self.safe_mode is False:
            raise RuntimeError("System is not in SAFE MODE.")

        if name not in self.modules:
            raise ValueError(f"Module '{name}' not found.")

        module = self.modules[name]
        return module.run(payload)

    def enable_safe_mode(self):
        self.safe_mode = True

    def disable_safe_mode(self):
        raise PermissionError("Safe mode cannot be disabled in CORE.")
