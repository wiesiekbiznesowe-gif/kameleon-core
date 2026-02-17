from core.orchestrator import Orchestrator
from core.engines.test import Engine
from core.engines.echo_engine import EchoEngine


def main():
    orchestrator = Orchestrator()

    # Rejestrujemy silniki
    orchestrator.register_module("test", Engine())
    orchestrator.register_module("echo", EchoEngine())

    # Test 1
    result1 = orchestrator.execute("test", {"message": "Start Kameleon"})
    print(result1)

    # Test 2
    result2 = orchestrator.execute("echo", {"message": "Kameleon rośnie"})
    print(result2)


if __name__ == "__main__":
    main()
