class UsageTracker:
    """
    Global usage control layer.
    Responsible for limiting module execution.
    """

    def __init__(self):
        self.global_limit = 100
        self.module_limits = {
            "test": 50,
            "echo": 50,
            "image": 10
        }

        self.global_count = 0
        self.module_counts = {}

        self.safe_mode_triggered = False

    def check_and_track(self, module_name: str) -> dict:
        if self.safe_mode_triggered:
            return {
                "allowed": False,
                "reason": "SAFE MODE ACTIVE"
            }

        # Global limit
        if self.global_count >= self.global_limit:
            self.safe_mode_triggered = True
            return {
                "allowed": False,
                "reason": "Global limit exceeded"
            }

        # Module limit
        module_limit = self.module_limits.get(module_name)

        if module_limit is not None:
            module_count = self.module_counts.get(module_name, 0)

            if module_count >= module_limit:
                return {
                    "allowed": False,
                    "reason": f"Module limit exceeded: {module_name}"
                }

        # Increment counters
        self.global_count += 1
        self.module_counts[module_name] = self.module_counts.get(module_name, 0) + 1

        return {
            "allowed": True
        }
