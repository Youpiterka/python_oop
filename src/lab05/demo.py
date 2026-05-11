from models import Warrior, Mage
from collection import CharacterCollection
from strategies import (
    by_name, by_level, by_damage,
    is_alive, is_warrior, is_strong,
    make_level_filter,
    get_name, buff,
    DamageBoost,
)


def print_all(collection):
    for c in collection:
        print(" ", c)


collection = CharacterCollection()
collection.add(Warrior("Aragorn", 100, 10, 25, 15, 20))
collection.add(Warrior("Boromir", 90, 8, 22, 12, 18))
collection.add(Mage("Gandalf", 80, 15, 18, 200, 30))
collection.add(Mage("Saruman", 75, 12, 30, 180, 28))
collection.add(Warrior("Gimli", 110, 7, 28, 20, 25))


collection.find_by_name("Boromir").take_damage(999)



print("\nИсходная коллекция")
print_all(collection)

print("\nСортировка по имени")
print_all(collection.sort_by(by_name))

print("\nСортировка по уровню")
print_all(collection.sort_by(by_level))

print("\nСортировка по урону")
print_all(collection.sort_by(by_damage))

print("\nФильтр: только живые")
print_all(collection.filter_by(is_alive))

print("\nФильтр: только воины")
print_all(collection.filter_by(is_warrior))




print("\nmap: получить имена всех персонажей")
names = list(map(get_name, collection))
print(" ", names)

print("\nФабрика функций: фильтр по уровню >= 10")
level_10_plus = make_level_filter(10)
print_all(collection.filter_by(level_10_plus))

print("\nСравнение: lambda и именованная функция дают то же самое")
print("Через by_name:")
print_all(collection.sort_by(by_name))
print("Через lambda:")
print_all(collection.sort_by(lambda c: c.name))


print("\nфильтр живых:")
step1 = collection.filter_by(is_alive)
print_all(step1)

print("\nсортировка по урону:")
step2 = step1.sort_by(by_damage)
print_all(step2)

print("\nвсем добавляем +10 к урону:")
step3 = step2.apply(buff)
print_all(step3)


print("\nСтратегия by_name:")
print_all(collection.sort_by(by_name))

print("\nСтратегия by_level:")
print_all(collection.sort_by(by_level))

print("\nСтратегия by_damage:")
print_all(collection.sort_by(by_damage))


fresh = CharacterCollection()
fresh.add(Warrior("Test1", 100, 5, 20, 10, 10))
fresh.add(Mage("Test2", 100, 5, 20, 100, 10))

print("\nДо применения стратегии:")
print_all(fresh)

boost_x2 = DamageBoost(2)        
fresh.apply(boost_x2)           

print("\nПосле DamageBoost(2):")
print_all(fresh)