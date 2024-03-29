# Семинары по Django от [GeekBrains](https://gb.ru)

## Содержание

- [Описание](#описание)
- [Настройка виртуального окружения](#настройка-виртуального-окружения)
- [Запуск приложений](#запуск-приложений)
- [Список семинаров](#список-семинаров)

## Описание

В этом репозитории находятся решения заданий с семинаров  по Django.

Задания с семинаров распределены по правилу: `app_<номер_семинара>/`.

Для каждого семинара отводится отдельное приложение, в котором содержится выполнение всех заданий.

Все модули отформатированы инструментом [Ruff](https://docs.astral.sh/ruff/) по настройкам в [ruff.toml](./ruff.toml)

В некоторых модулях представлены результаты выполнения сразу нескольких заданий.

Различить их можно по количеству отделённых друг от друга блоков комментариев с заданиями.

Например, в модуле с такими комментариями:

```python
# Написать функцию, которая будет принимать
# на вход два числа и выводить на экран их сумму.
```

Содержится решение только одного задания.

А в модуле с такими комментариями:

```python
# Напишите простое веб-приложение на Django, которое будет
# выводить на экран текст "Hello, World!".

# Добавьте две дополнительные страницы в ваше веб-приложение:
# страницу "about" и страницу "contact".
```

Содержится решение двух заданий.

## Настройка виртуального окружения

Для настройки виртуального окружения используйте команду 

`py -m venv <название_виртуального_окружения>`

(`python -m venv <название_виртуального_окружения>` на Windows или `python3 -m venv <название_виртуального_окружения>` на Linux, если основная команда не работает)

После этого, активируйте виртуальное окружение командой для вашей ОС.

Для установки необходимых зависимостей, при активном виртуальном окружении выполните команду

`pip install -r requirements.txt`

[Список зависимостей](./requirements.txt):

| Библиотека | Версия |
|---|---|
| ruff | >=0.1.11 |
| Django | >= 5.0.1 |

Виртуальное окружение настроено!

## Запуск приложений

Для запуска сервера и проверки приложений используйте команду 

`py manage.py runserver`

(`python manage.py runserver` на Windows или `python3 manage.py runserver` на Linux, если основная команда не работает)

## Список семинаров

- [Семинар 1](./app_1/) ДЗ: Задание 8
- [Семинар 2](./app_1/), [модели](./app_1/models.py), [команды](./app_1/management/commands/), ДЗ: Задание 8