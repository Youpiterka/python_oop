class Character:
    max_level: int = 100  # атрибут класса

    def __init__(self, name: str, health: int, level: int, damage: int) -> None:
        self._name: str = self._validate_name(name)
        self._health: int = self._validate_health(health)
        self._level: int = self._validate_level(level)
        self._damage: int = self._validate_damage(damage)
        self._experience: int = 0
        self._alive: bool = True

    # валидация
    def _validate_name(self, value: str) -> str:
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Имя должно быть непустой строкой")
        return value

    def _validate_health(self, value: int) -> int:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Здоровье должно быть положительным")
        return value

    def _validate_level(self, value: int) -> int:
        if not isinstance(value, int) or value < 1 or value > Character.max_level:
            raise ValueError(f"Уровень должен быть от 1 до {Character.max_level}")
        return value

    def _validate_damage(self, value: int) -> int:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Урон не может быть отрицательным")
        return value

    # properties
    @property
    def name(self) -> str:
        return self._name

    @property
    def health(self) -> int:
        return self._health

    @property
    def level(self) -> int:
        return self._level

    @property
    def damage(self) -> int:
        return self._damage

    @damage.setter
    def damage(self, value: int) -> None:
        self._damage = self._validate_damage(value)

    @property
    def experience(self) -> int:
        return self._experience

    # магические методы
    def __str__(self) -> str:
        status = "alive" if self._alive else "dead"
        return f"{self._name} | lvl {self._level} | HP {self._health} | dmg {self._damage} | {status}"

    def __repr__(self) -> str:
        return f"Character(name='{self._name}', health={self._health}, level={self._level}, damage={self._damage})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Character):
            return False
        return self._name == other._name and self._level == other._level

    # бизнес методы
    def attack(self, other: "Character") -> None:
        if not self._alive:
            raise RuntimeError("Мёртвый персонаж не может атаковать")
        other.take_damage(self._damage)

    def take_damage(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Урон не может быть отрицательным")
        self._health -= amount
        if self._health <= 0:
            self._health = 0
            self._alive = False

    def gain_experience(self, exp: int) -> None:
        if exp < 0:
            raise ValueError("Опыт не может быть отрицательным")
        self._experience += exp
        if self._experience >= 100:
            self._experience -= 100
            self.level_up()

    def level_up(self) -> None:
        if self._level < Character.max_level:
            self._level += 1
            self._damage += 5

    def calculate_power(self) -> int:
        return self._damage + self._level

class Displayable(Protocol):
    def display(self) -> str: ...

class Scorable(Protocol):
    def score(self) -> float: ...
