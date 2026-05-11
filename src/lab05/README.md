# ЛР-5 — Функции как аргументы

## 1. Цель работы
Научиться передавать функции как аргументы, использовать map/filter/sorted,
lambda, фабрики функций и паттерн Стратегия через callable-объекты.

## 2. Что реализовано

### strategies.py
- Сортировки: by_name, by_level, by_damage
- Фильтры: is_alive, is_warrior, is_strong
- Фабрика: make_level_filter(min_level)
- Обработчики: get_name, buff
- Callable-стратегия: DamageBoost

### collection.py
В коллекцию добавлены методы:
- sort_by(key_func) — сортировка
- filter_by(predicate) — фильтрация
- apply(func) — применить функцию ко всем

## 3. Демонстрация
- Исходная коллекция + сортировки по имени и уровню
![](https://github.com/Youpiterka/python_oop/blob/main/misc/img/lab5img/Снимок%20экрана%202026-05-11%20142718.png)


- Фильтры: только живые и только воины
![](https://github.com/Youpiterka/python_oop/blob/main/misc/img/lab5img/Снимок%20экрана%202026-05-11%20142744.png)


- map получить имена всех персонажей + фабрика фильтр по уровню
 ![](https://github.com/Youpiterka/python_oop/blob/main/misc/img/lab5img/Снимок%20экрана%202026-05-11%20142816.png)




- всем +10 к урону
![](https://github.com/Youpiterka/python_oop/blob/main/misc/img/lab5img/Снимок%20экрана%202026-05-11%20143055.png)




- Стратегии
![](https://github.com/Youpiterka/python_oop/blob/main/misc/img/lab5img/Снимок%20экрана%202026-05-11%20143115.png)
![](https://github.com/Youpiterka/python_oop/blob/main/misc/img/lab5img/Снимок%20экрана%202026-05-11%20143121.png)


## 4. Вывод
Изучил: передачу функций аргументами, lambda, map/filter/sorted,
фабрики функций, паттерн Стратегия через __call__, цепочки методов.
