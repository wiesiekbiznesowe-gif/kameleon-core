from core.orchestrator import Orchestrator
from core.engines.test import Engine
from core.engines.echo_engine import EchoEngine


def main():
    orchestrator = Orchestrator()

    # Rejestrujemy silniki
    orchestrator.register_module("test", Engine())
    orchestrator.register_module("echo", EchoEngine())

    # Test 1 – normal execution
    result1 = orchestrator.execute("test", {"message": "Start Kameleon"})
    print("TEST 1:", result1)

    # Test 2 – normal execution
    result2 = orchestrator.execute("echo", {"message": "Kameleon rośnie"})
    print("TEST 2:", result2)

    # Test 3 – Guard BLOCK test (za długi message)
    long_message = "A" * 2000
    result3 = orchestrator.execute("test", {"message": long_message})
    print("TEST 3:", result3)


if __name__ == "__main__":
    main()
