from abc import ABC, abstractmethod


class BaseEngine(ABC):

    @abstractmethod
    def run(self, payload: dict) -> dict:
        pass
