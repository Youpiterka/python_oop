from model import Character

# сценарий 1: создание и вывод
hero = Character("V", 100, 1, 15)
enemy = Character("Drone", 60, 1, 10)

print(hero)
print(enemy)

# сценарий 2: сравнение объектов
print("Равные:", hero == enemy)

# сценарий 3: атака
hero.attack(enemy)
print("Противник после атаки:", enemy)

# сценарий 4: изменение свойства через setter
hero.damage = 25
print("Новый урон:", hero.damage)

# сценарий 5: доступ к атрибуту класса
print("Max level:", Character.max_level)
print("Max level через объект:", hero.max_level)

# сценарий 6: проверка валидации
try:
    bad = Character("", -10, 0, -5)
except Exception as e:
    print("название ошибки:", e)

# сценарий 7: логическое состояние
enemy.take_damage(100)
print("Враг против фатального урона:", enemy)

try:
    enemy.attack(hero)
except Exception as e:
    print(e)