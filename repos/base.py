# python
from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseFlow(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Process a JSON-like payload and return a JSON-serializable dict."""
        raise NotImplementedError