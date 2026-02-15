from core.orchestrator import Orchestrator
from core.engines.test_engine import TestEngine

# Tworzymy orchestrator
orch = Orchestrator()

# Rejestrujemy moduł
orch.register_module("test", TestEngine())

# Wykonujemy test
result = orch.execute("test", {"message": "Kameleon działa"})

print(result)
