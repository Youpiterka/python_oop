from model import Character
from collection import CharacterCollection

col = CharacterCollection()

# создание персонажей
c1 = Character("V", 100, 1, 15)
c2 = Character("Drone", 60, 1, 10)
c3 = Character("Witcher", 150, 30, 40)
c4 = Character("Hacker", 80, 55, 20)
c5 = Character("Boss", 300, 99, 80)

# добавление в коллекцию
col.add(c1)
col.add(c2)
col.add(c3)
col.add(c4)
col.add(c5)

print("Все персонажи:")
print(col)

# удаление одного
col.remove(c2)
print("\nПосле удаления Drone:")
print(col)

# поиск
print("\nИщем Witcher:", col.find_by_name("Witcher"))
print("Персонажи 1 уровня:", col.find_by_level(1))

# len и for
print(f"\nВсего персонажей: {len(col)}")
print("Перебираем через for:")
for char in col:
    print(" ", char)

# индексация
print(f"\ncol[0] = {col[0]}")
print(f"col[1] = {col[1]}")

# сортировка
col.sort_by_level()
print("\nПосле сортировки по уровню:")
for char in col:
    print(" ", char)

# убиваем V чтобы показать фильтрацию
c1.take_damage(9999)

# удаление по индексу
col.remove_at(0)
print(f"\nУдалили первого (V), осталось: {len(col)}")

# добавление мёртвого V обратно для демонстрации фильтрации
col.add(c1)

# фильтрация
print("\nЖивые персонажи:")
for char in col.get_alive():
    print(" ", char)

print("\nМёртвые персонажи:")
for char in col.get_dead():
    print(" ", char)

print("\nВысокоуровневые (lvl >= 50):")
for char in col.get_high_level(50):
    print(" ", char)

# проверка защит
print("\n--- проверка защит ---")

try:
    col.add("просто строка")
except TypeError as e:
    print("неверный тип:", e)

try:
    col.add(Character("Boss", 100, 1, 5))
except ValueError as e:
    print("дубликат:", e)

try:
    col.remove(Character("Призрак", 100, 1, 5))
except ValueError as e:
    print("удаление несуществующего:", e)

try:
    col.remove_at(999)
except IndexError as e:
    print("неверный индекс:", e)
