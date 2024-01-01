from abc import ABC, abstractmethod


class BaseModel:
    def __init__(self, uuid):
        self.uuid = uuid
        self.history = []

    @abstractmethod
    def chat(self, messages) -> str:
        pass

    @abstractmethod
    def clear_history(self) -> None:
          self.history = []
