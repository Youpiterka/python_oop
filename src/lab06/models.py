from base import Character


class Warrior(Character):
    def __init__(self, name: str, health: int, level: int, damage: int,
                 armor: int, stamina: int) -> None:
        super().__init__(name, health, level, damage)
        self._armor: int = self.validate_armor(armor)
        self._stamina: int = self.validate_stamina(stamina)

    def validate_stamina(self, value: int) -> int:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Стамина должна быть положительным числом")
        return value

    def validate_armor(self, value: int) -> int:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Броня должна быть положительным числом")
        return value

    def strong_hit(self) -> int:
        return self.damage * 2

    def calculate_power(self) -> int:
        return self.damage + self._armor + self._stamina

    def __str__(self) -> str:
        return super().__str__() + f" | armor {self._armor} | stamina {self._stamina}"


class Mage(Character):
    def __init__(self, name: str, health: int, level: int, damage: int,
                 mana: int, intellegence: int) -> None:
        super().__init__(name, health, level, damage)
        self._mana: int = self.validate_mana(mana)
        self._intellegence: int = self.validate_intellegence(intellegence)

    def validate_mana(self, value: int) -> int:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Мана должна быть положительным числом")
        return value

    def validate_intellegence(self, value: int) -> int:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Интеллект должен быть положительным числом")
        return value

    def magic_hit(self) -> float:
        return self.damage * self._intellegence * 0.15

    def calculate_power(self) -> int:
        return self.damage + self._mana + self._intellegence

    def __str__(self) -> str:
        return super().__str__() + f" | mana {self._mana} | intellegence {self._intellegence}"