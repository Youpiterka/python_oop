from models import Warrior, Mage
from base import Character
from interfaces import Printable, Comparable

class CharacterCollection:
    def __init__(self):
        self._items = []
            

    def add(self, item):
        if  not isinstance(item, Character):
            raise ValueError
        for i in self._items:
            if item == i:
                raise ValueError("Такой персонаж уже существует")
        self._items.append(item)
    

    def remove(self, item):
        self._items.remove(item)

    def get_all(self):
        return self._items
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)

    def find_by_name(self, name):
        for item in self._items:
            if item.name == name:
                return item
        return None
    
    def __getitem__(self, index):
        return self._items[index]
    
    def remove_at(self, index):
        del self._items[index]

    def sort_by_lvl(self):
        self._items.sort(key= lambda item: item.level)

    def get_alive(self):
        new_collection = CharacterCollection()
        for c in self._items:
            if c._alive:
                new_collection.add(c)
        return new_collection
    
    
    def get_only_warriors(self):
        return [x for x in self._items if isinstance(x, Warrior)]

    
    def get_only_mages(self):
        return [x for x in self._items if isinstance(x, Mage)]
    

    def get_printable(self):
        return [x for x in self._items if isinstance(x, Printable)]
    

    def get_comparable(self):
        return [x for x in self._items if isinstance(x, Comparable)]

    def print_all(self):
        for item in self.get_printable():
            print(item.to_string())

    def sort_by_power(self):
        items = self.get_comparable()
        n = len(items)
        for i in range(n):
            for j in range(0, n - i - 1):
                if items[j].compare_to(items[j + 1]) == 1:
                    items[j], items[j + 1] = items[j + 1], items[j]
        return items