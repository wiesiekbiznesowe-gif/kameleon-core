from core.orchestrator import Orchestrator
from core.engines.test import Engine


def main():
    orchestrator = Orchestrator()

    orchestrator.register_module("test", Engine())

    result = orchestrator.execute("test", {"message": "Start Kameleon"})
    print(result)


if __name__ == "__main__":
    main()
