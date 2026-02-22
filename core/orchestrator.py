def execute(self, name: str, payload: Dict) -> Dict:
    if not self.safe_mode:
        raise RuntimeError("System is not in SAFE MODE.")

    if name not in self.modules:
        return {
            "status": "error",
            "engine": name,
            "data": None,
            "error": f"Module '{name}' not found."
        }

    module = self.modules[name]

    try:
        result = module.run(payload)

        # Walidacja formatu odpowiedzi
        if not isinstance(result, dict):
            raise ValueError("Invalid engine response format.")

        required_keys = {"status", "engine", "data", "error"}
        if not required_keys.issubset(result.keys()):
            raise ValueError("Engine response missing required keys.")

        return result

    except Exception as e:
        return {
            "status": "error",
            "engine": name,
            "data": None,
            "error": str(e)
        }
