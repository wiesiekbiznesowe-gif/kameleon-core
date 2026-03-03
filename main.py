from core.orchestrator import Orchestrator
from core.engines.test_engine import Engine
from core.engines.echo_engine import EchoEngine
from core.engines.image_engine import ImageEngine


def main():
    orchestrator = Orchestrator()

    # Rejestrujemy silniki
    orchestrator.register_module("test", Engine())
    orchestrator.register_module("echo", EchoEngine())
    orchestrator.register_module("image", ImageEngine())

    # Test 1
    result1 = orchestrator.execute("test", {"message": "Start Kameleon"})
    print("TEST 1:", result1)

    # Test 2
    result2 = orchestrator.execute("echo", {"message": "Kameleon rośnie"})
    print("TEST 2:", result2)

    # Test 3 - IMAGE ENGINE
    result3 = orchestrator.execute("image", {"prompt": "Architekt przyszłości"})
    print("TEST 3:", result3)


if __name__ == "__main__":
    main()
