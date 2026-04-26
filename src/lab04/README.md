# Лабораторная работа №4 — Интерфейсы и абстрактные классы

## 1. Цель работы

Изучить:
- абстрактные базовые классы (ABC) в Python;
- понятие интерфейса как контракта поведения;
- полиморфизм через единый интерфейс;
- множественную реализацию интерфейсов;
- интеграцию интерфейсов с коллекцией.

## 2. Описание интерфейсов

В файле `interfaces.py` созданы два интерфейса через `ABC`:

### `Printable`
Контракт: класс умеет представлять себя строкой.
Обязательный метод:
- `to_string()` — вернуть строковое представление.

### `Comparable`
Класс сравнивает себя с другим объектом.
Обязательный метод:
- `compare_to(other)` — вернуть `-1`, `0` или `1`.

Оба интерфейса используют декоратор `@abstractmethod` — наследник
обязан реализовать эти методы, иначе Python не даст создать объект.

## 3. Реализация в классах

Интерфейсы реализуют два класса — `Warrior` и `Mage` (`models.py`).
Оба сразу наследуются от `Character` и от двух интерфейсов:

    class Warrior(Character, Printable, Comparable):
    class Mage(Character, Printable, Comparable):

Это и есть множественная реализация интерфейсов.

**Разное поведение `to_string()`:**
- Warrior: `Воин Geralt, уровень 5, броня 15, сила 65`
- Mage:    `Маг Yennefer, уровень 5, мана 50, сила 102`

**Разное поведение `compare_to()`:**
оба сравнивают по `calculate_power()`, который у каждого класса свой:
- у воина: `damage + armor + stamina`;
- у мага:  `damage + mana + intellegence`.

## 4. Коллекция и интеграция с интерфейсами

`CharacterCollection` в неё добавлены методы для работы через интерфейсы:

- `get_printable()` — фильтрует объекты по интерфейсу `Printable`;
- `get_comparable()` — фильтрует по интерфейсу `Comparable`;
- `print_all()` — полиморфный вывод (без `isinstance` и условий);
- `sort_by_power()` — сортировка через `compare_to` интерфейса `Comparable`.

## 5. Демонстрация


### Метод to_string у разных классов и Сравнение через compare_to

![](https://github.com/Youpiterka/python_oop/blob/main/misc/img/LAB4_IMGG/Снимок%20экрана%202026-04-26%20151756.png)

### функция print_all

![](https://github.com/Youpiterka/python_oop/blob/main/misc/img/LAB4_IMGG/Снимок%20экрана%202026-04-26%20151936.png)


### Проверка через isinstance

![](https://github.com/Youpiterka/python_oop/blob/main/misc/img/LAB4_IMGG/Снимок%20экрана%202026-04-26%20152949.png)

### фильтрация по Printable и вывод всех через Printable

![](https://github.com/Youpiterka/python_oop/blob/main/misc/img/LAB4_IMGG/Снимок%20экрана%202026-04-26%20153415.png)


###сортировка по силе через Comparable

![](https://github.com/Youpiterka/python_oop/blob/main/misc/img/LAB4_IMGG/Снимок%20экрана%202026-04-26%20153423.png)
