class Guard:

    MAX_MESSAGE_LENGTH = 1000

    @staticmethod
    def validate(module_name: str, payload: dict) -> dict:
        """
        Global validation layer for all engine inputs.
        Returns:
            { "allowed": True }
        or
            { "allowed": False, "error": "reason" }
        """

        if not isinstance(payload, dict):
            return {
                "allowed": False,
                "error": "Payload must be a dictionary."
            }

        # Basic example rule: message length limit
        message = payload.get("message")

        if message and len(message) > Guard.MAX_MESSAGE_LENGTH:
            return {
                "allowed": False,
                "error": "Message exceeds maximum allowed length."
            }

        return {
            "allowed": True
        }
