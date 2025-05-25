from abs import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')
ID = TypeVar('ID')  # Data type for the model


class AbstractRepository(ABC, Generic[T, ID]):
    """
    Abstract base class for repository pattern.
    """

    @abstractmethod
    async def get(self, id: ID) -> Optional[T]:
        """
        Get an object by its ID.
        """
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        """
        Get all objects with pagination.
        """
        pass

    @abstractmethod
    async def create(self, obj: T) -> T:
        """
        Create a new object.
        """
        pass

    @abstractmethod
    async def update(self, id: ID, obj: T) -> Optional[T]:
        """
        Update an existing object.
        """
        pass

    @abstractmethod
    async def delete(self, id: ID) -> bool:
        """
        Delete an object by its ID.
        """
        pass 