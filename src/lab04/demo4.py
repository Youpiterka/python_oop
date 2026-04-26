from models import Warrior, Mage
from collection1 import CharacterCollection
from interfaces import Printable, Comparable




warrior = Warrior("Thor", 120, 5, 20, 15, 30)
mage = Mage("Marlin", 80, 5, 12, 50, 40)

print("Метод to_string у воина:")
print(warrior.to_string())

print("Метод to_string у мага:")
print(mage.to_string())

print("Сравнение через compare_to:")
result = warrior.compare_to(mage)
if result == 1:
    print("Воин сильнее мага")
elif result == -1:
    print("Маг сильнее воина")
else:
    print("Силы равны")




def print_all(items):
    for item in items:
        print(item.to_string())

print("\nфункция print_all:")
print_all([warrior, mage])

print("\nПроверка через isinstance:")
print("Воин — Printable?", isinstance(warrior, Printable))
print("Воин — Comparable?", isinstance(warrior, Comparable))
print("Маг — Printable?", isinstance(mage, Printable))
print("Маг — Comparable?", isinstance(mage, Comparable))




collection = CharacterCollection()
collection.add(Warrior("Geralt", 120, 5, 20, 15, 30))
collection.add(Mage("Yennefer", 80, 5, 12, 50, 40))
collection.add(Warrior("Lambert", 100, 3, 18, 10, 25))
collection.add(Mage("Triss", 70, 4, 14, 45, 35))

print("\nВсего персонажей:", len(collection))


print("\nфильтрация по Printable:")
printable_items = collection.get_printable()
print(len(printable_items))


print("\nвывод всех через Printable:")
collection.print_all()


print("\nсортировка по силе через Comparable:")
sorted_chars = collection.sort_by_power()
for ch in sorted_chars:
    print(ch.to_string())
