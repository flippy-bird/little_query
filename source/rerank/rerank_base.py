from abc import ABC, abstractmethod

class BaseReranker(ABC):
    @abstractmethod
    def rerank(self, query: str, chunks: list[str]) -> list[str]:
        raise NotImplementedError