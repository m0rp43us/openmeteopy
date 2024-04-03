from abc import ABC, abstractmethod

class Option(ABC):
    @abstractmethod
    def get_api_path(self):
        pass
    @abstractmethod
    def get_payload(self):
        pass