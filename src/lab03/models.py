from base import Character

class Warrior(Character):
    def __init__(self, name, health, level, damage, armor, stamina):
        super().__init__(name, health, level, damage)
        self._armor = self.validate_armor(armor)
        self._stamina = self.validate_stamina(stamina)

    def validate_stamina(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Стамина должна быть положительным числом")
        return value
        
    def validate_armor(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Броня должна быть положительным числом")
        return value
    

    def strong_hit(self):
        return self.damage * 2
    
    def calculate_power(self):
        return self.damage + self._armor + self._stamina
    
    def __str__(self):
        return super().__str__() + f" | armor {self._armor} | stamina {self._stamina}"
    

class Mage(Character):
    def __init__(self, name, health, level, damage, mana, intellegence):
        super().__init__(name, health, level, damage)
        self._mana = self.validate_mana(mana)
        self._intellegence = self.validate_intellegence(intellegence)


    def validate_mana(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Мана должна быть положительным числом")
        return value
    
    def validate_intellegence(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Интеллект должен быть положительным числом")
        return value

    def magic_hit(self):
        return self.damage * self._intellegence * 0.15
    
    def calculate_power(self):
        return self.damage + self._mana + self._intellegence
    
    def __str__(self):
        return super().__str__() + f" | mana {self._mana} | intellegence {self._intellegence}"