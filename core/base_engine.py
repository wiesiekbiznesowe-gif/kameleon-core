from abc import ABC, abstractmethod
from datetime import datetime


class BaseEngine(ABC):

    VERSION = "1.0"

    def run(self, payload: dict) -> dict:
        try:
            result = self._execute(payload)

            return {
                "status": "success",
                "engine": self.__class__.__name__.lower(),
                "version": self.VERSION,
                "timestamp": datetime.utcnow().isoformat(),
                "data": result,
                "error": None
            }

        except Exception as e:
            return {
                "status": "error",
                "engine": self.__class__.__name__.lower(),
                "version": self.VERSION,
                "timestamp": datetime.utcnow().isoformat(),
                "data": None,
                "error": {
                    "code": "ENGINE_RUNTIME_ERROR",
                    "message": str(e)
                }
            }

    @abstractmethod
    def _execute(self, payload: dict):
        pass
