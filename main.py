from core.orchestrator import Orchestrator

def main():
    orchestrator = Orchestrator()
    result = orchestrator.execute("test", {"message": "Start Kameleon"})
    print(result)

if __name__ == "__main__":
    main()
