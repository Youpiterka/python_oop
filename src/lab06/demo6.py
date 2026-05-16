from base import Character
from models import Warrior, Mage
from container import TypedCollection, Displayable, Scorable



print("Сценарий 1: TypedCollection[Character] и добавление объектов")

col: TypedCollection[Character] = TypedCollection()
col.add(Warrior("Borin", 150, 7, 25, 12, 30))
col.add(Mage("Lyra", 80, 5, 18, 40, 22))
col.add(Warrior("Maximus", 120, 10, 30, 20, 25))

print("Всего:", len(col))

try:
    col.add(Warrior("Borin", 150, 7, 25, 12, 30))
except ValueError as e:
    print("Ошибка:", e)

print("Все элементы:")
for c in col.get_all():
    print(" ", c)

# Демонстрация валидации параметров при создании объекта
try:
    bad = Warrior("Bad", 50, 2, 5, -5, 10)  # некорректная броня
    col.add(bad)
except ValueError as e:
    print("Ошибка валидации при создании персонажа:", e)



print()
print("Сценарий 2: Операции поиска/фильтрации/проекций (find/filter/map) ")

found = col.find(lambda c: c.calculate_power() > 20)
print("find damage>20:", found)

not_found = col.find(lambda c: c.level > 50)
print("find level>50:", not_found)

filtered = col.filter(lambda c: c.level >= 7)
print("filter level>=7:")
for c in filtered:
    print(" ", c)

names = col.map(lambda c: c.name)
powers = col.map(lambda c: float(c.calculate_power()))
print("map -> имена (list[str]):", names)
print("  element type:", type(names[0]).__name__ if names else None)
print("map -> сила  (list[float]):", powers)
print("  element type:", type(powers[0]).__name__ if powers else None)



print()

print("Сценарий 3: TypedCollection[Displayable] объекты из иерархии ЛР-3")
col2: TypedCollection[Displayable] = TypedCollection()
col2.add(Warrior("Borin", 150, 7, 25, 12, 30))
col2.add(Mage("Lyra", 80, 5, 18, 40, 22))
col2.add(Character("Aldric", 100, 3, 15))
for d in col2.get_all():
    print(" ", d.display())

print()
print("Сценарий 4: TypedCollection[Scorable] тот же TypedCollection с другим Protocol")
col3: TypedCollection[Scorable] = TypedCollection()
col3.add(Warrior("Maximus", 120, 10, 30, 20, 25))
col3.add(Mage("Zara", 70, 6, 20, 55, 30))
for s in col3.get_all():
    print("  score =", s.score())

