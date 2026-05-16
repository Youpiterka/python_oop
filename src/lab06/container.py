from typing import TypeVar, Generic, Callable, Optional, Protocol


# два протокола

class Displayable(Protocol):
    def display(self) -> str:
        pass


class Scorable(Protocol):
    def score(self) -> float:
        pass


# TypeVar-ы

T = TypeVar("T")
R = TypeVar("R")
D = TypeVar("D", bound=Displayable)
S = TypeVar("S", bound=Scorable)


# Generic-коллекция

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        for i in self._items:
            if item == i:
                raise ValueError("Такой элемент уже существует")
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return self._items

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def remove_at(self, index: int) -> None:
        del self._items[index]

    def __iter__(self):
        return iter(self._items)

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        result: list[T] = []
        for item in self._items:
            if predicate(item):
                result.append(item)
        return result

    def map(self, transform: Callable[[T], R]) -> list[R]:
        result: list[R] = []
        for item in self._items:
            result.append(transform(item))
        return result
