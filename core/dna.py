class SystemDNA:
    """
    Niezmienna warstwa zasad systemu Kameleon.
    """

    def __init__(self):
        self.mode = "LOCAL_ONLY"
        self.max_payload = 5000
        self.system_locked = False

    def authorize(self, module, payload):

        if self.system_locked:
            return {
                "allowed": False,
                "reason": "System locked by DNA"
            }

        payload_str = str(payload)

        if len(payload_str) > self.max_payload:
            return {
                "allowed": False,
                "reason": "Payload too large"
            }

        return {
            "allowed": True
        }

    def lock_system(self):
        self.system_locked = True

    def unlock_system(self):
        self.system_locked = False
