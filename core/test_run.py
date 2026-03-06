from core.orchestrator import Orchestrator


def main():

    system = Orchestrator()

    result = system.run(
        "image",
        {
            "prompt": "first kameleon test"
        }
    )

    print(result)


if __name__ == "__main__":
    main()
