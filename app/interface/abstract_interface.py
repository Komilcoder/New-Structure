
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')  #T — bu model obyektining turi (User, Organization, Region, va hokazo).
ID = TypeVar('ID') #ID — bu modelning ID (primary key) tipi (int, UUID, str, va hokazo).


class AbstractRepository(ABC, Generic[T, ID]):
    @abstractmethod
    async def get(self, id: ID) -> Optional[T]: ...
    
    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[T]: ...
    
    @abstractmethod
    async def create(self, obj: T) -> T: ...
    
    @abstractmethod
    async def update(self, id: ID, obj: T) -> Optional[T]: ...
    
    @abstractmethod
    async def delete(self, id: ID) -> bool: ...

