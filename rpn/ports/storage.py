from abc import ABC, abstractmethod


class StorageInterface(ABC):
    """Storage interface that should be implemented by our storage systems"""

    @abstractmethod
    def append_value(self, stack_id: str, value: float) -> dict:
        raise NotImplementedError

    @abstractmethod
    def pop_value(self, stack_id: str) -> float:
        raise NotImplementedError

    @abstractmethod
    def read_stack(self, stack_id: str) -> dict | None:
        raise NotImplementedError

    @abstractmethod
    def delete_stack(self, stack_id: str) -> None:
        raise NotImplementedError