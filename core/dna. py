class SystemDNA:
    """
    Immutable system rules layer.
    Acts as a constitutional validator before execution.
    """

    def __init__(self):
        self.mode = "LOCAL_ONLY"  # LOCAL_ONLY | HYBRID | EXTERNAL_ALLOWED
        self.max_payload_size = 5000
        self.system_locked = False

    def validate(self, module_name: str, payload: dict) -> dict:
        if self.system_locked:
            return {
                "allowed": False,
                "reason": "System is locked by DNA"
            }

        # Payload size validation
        payload_str = str(payload)
        if len(payload_str) > self.max_payload_size:
            return {
                "allowed": False,
                "reason": "Payload too large (DNA rule)"
            }

        # Mode enforcement
        if self.mode == "LOCAL_ONLY":
            # In future we mark engines as external/local
            # For now assume all engines are LOCAL
            pass

        return {
            "allowed": True
        }

    def lock_system(self):
        self.system_locked = True

    def unlock_system(self):
        self.system_locked = False
