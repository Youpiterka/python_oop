from models import Warrior, Mage
from collection1 import CharacterCollection

w = Warrior("Thor", 120, 5, 20, 10, 15)
m = Mage("Marlin", 100, 6, 15, 30, 20)

print(w)
print(m)

print(w.strong_hit())
print(m.magic_hit())

team = [w, m]

print("Сила персонажей")
for hero in team:
    print(hero.calculate_power())


print("Все персонажи")
for hero in team:
    print(hero)

collection = CharacterCollection()
collection.add(w)
collection.add(m)

print("Только воины")
for hero in collection.get_only_warriors():
    print(hero)

print("Только маги")
for hero in collection.get_only_mages():
    print(hero)