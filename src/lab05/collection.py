from base import Character


class CharacterCollection:
    def __init__(self, items=None):
        if items is None:
            self._items = []
        else:
            self._items = list(items)

    def add(self, item):
        if not isinstance(item, Character):
            raise ValueError("Можно добавлять только Character")
        for i in self._items:
            if item == i:
                raise ValueError("Такой персонаж уже существует")
        self._items.append(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def find_by_name(self, name):
        for item in self._items:
            if item.name == name:
                return item
        return None


    def sort_by(self, key_func):
        new_items = sorted(self._items, key=key_func)
        return CharacterCollection(new_items)

    def filter_by(self, predicate):
        new_items = list(filter(predicate, self._items))
        return CharacterCollection(new_items)

    def apply(self, func):
        for item in self._items:
            func(item)
        return self