class Character:
    max_level = 100  # атрибут класса

    def __init__(self, name: str, health: int, level: int, damage: int):
        self._name = self._validate_name(name)
        self._health = self._validate_health(health)
        self._level = self._validate_level(level)
        self._damage = self._validate_damage(damage)
        self._experience = 0
        self._alive = True

    # валидация
    def _validate_name(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Имя должно быть непустой строкой")
        return value

    def _validate_health(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Здоровье должно быть положительным")
        return value

    def _validate_level(self, value):
        if not isinstance(value, int) or value < 1 or value > Character.max_level:
            raise ValueError(f"Уровень должен быть от 1 до {Character.max_level}")
        return value

    def _validate_damage(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Урон не может быть отрицательным")
        return value

    # properties
    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def level(self):
        return self._level

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = self._validate_damage(value)

    @property
    def experience(self):
        return self._experience

    # магические методы
    def __str__(self):
        status = "alive" if self._alive else "dead"
        return f"{self._name} | lvl {self._level} | HP {self._health} | dmg {self._damage} | {status}"

    def __repr__(self):
        return f"Character(name='{self._name}', health={self._health}, level={self._level}, damage={self._damage})"

    def __eq__(self, other):
        if not isinstance(other, Character):
            return False
        return self._name == other._name and self._level == other._level

    # бизнес методы
    def attack(self, other):
        if not self._alive:
            raise RuntimeError("Мёртвый персонаж не может атаковать")
        other.take_damage(self._damage)

    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Урон не может быть отрицательным")
        self._health -= amount
        if self._health <= 0:
            self._health = 0
            self._alive = False

    def gain_experience(self, exp):
        if exp < 0:
            raise ValueError("Опыт не может быть отрицательным")
        self._experience += exp
        if self._experience >= 100:
            self._experience -= 100
            self.level_up()
            

# состояние проверка максимального уровня
max_char = Character("Maximus", 120, Character.max_level, 30)

print("Персонаж на максимальном уровне:", max_char)

try:
    max_char.level_up()
except Exception as e:
    print("Ошибка повышения уровня:", e)
