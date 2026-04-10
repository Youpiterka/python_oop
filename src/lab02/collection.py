
from model import Character


class CharacterCollection:
    def __init__(self):
        self._items = []


    def add(self, item):
        if not isinstance(item, Character):
            raise TypeError("можно добавлять только объекты Character")

        for c in self._items:
            if c.name == item.name:
                raise ValueError(f"персонаж с именем '{item.name}' уже есть в коллекции")

        self._items.append(item)

    def remove(self, item):
        if item not in self._items:
            raise ValueError("такого персонажа нет в коллекции")
        self._items.remove(item)

    def get_all(self):
        return list(self._items)

    def find_by_name(self, name):
        for c in self._items:
            if c.name.lower() == name.lower():
                return c
        return None

    def find_by_level(self, level):
        result = []
        for c in self._items:
            if c.level == level:
                result.append(c)
        return result

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)


    def __getitem__(self, index):
        return self._items[index]

    def remove_at(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("индекс за пределами коллекции")
        self._items.pop(index)

    def sort_by_name(self):
        self._items.sort(key=lambda c: c.name.lower())

    def sort_by_level(self):
        self._items.sort(key=lambda c: c.level)

    def sort_by_health(self):
        self._items.sort(key=lambda c: c.health)

    def sort(self, key):
        self._items.sort(key=key)

    def get_alive(self):
        new_col = CharacterCollection()
        for c in self._items:
            if c.alive:
                new_col._items.append(c)
        return new_col

    def get_dead(self):
        new_col = CharacterCollection()
        for c in self._items:
            if not c.alive:
                new_col._items.append(c)
        return new_col

    def get_high_level(self, min_level=50):
        new_col = CharacterCollection()
        for c in self._items:
            if c.level >= min_level:
                new_col._items.append(c)
        return new_col

    def __str__(self):
        if len(self._items) == 0:
            return "Коллекция пуста"
        result = f"Коллекция персонажей ({len(self._items)} шт.):\n"
        for c in self._items:
            result += f"  {c}\n"
        return result.strip()
