"""Стратегии сортировки, фильтры и функции-обработчики."""

from models import Warrior, Mage

def by_name(character):
    return character.name


def by_level(character):
    return character.level


def by_damage(character):
    return character.damage



def is_alive(character):
    return character._alive


def is_warrior(character):
    return isinstance(character, Warrior)


def is_strong(character):
    return character.damage >= 20


def make_level_filter(min_level):
    def check(character):
        return character.level >= min_level
    return check


def get_name(character):
    return character.name


def buff(character):
    character.damage = character.damage + 10
    return character


class DamageBoost:

    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, character):
        character.damage = int(character.damage * self.multiplier)
        return character