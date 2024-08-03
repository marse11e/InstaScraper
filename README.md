# InstaScraper

InstaScraper - это инструмент на Python, который позволяет загружать и сохранять информацию о профиле и постах из Instagram, используя библиотеку `instaloader`. В проекте реализованы две основные функции: `information_profile()` для скачивания информации о профиле и `get_profile_posts()` для скачивания постов.

## Содержание

- [Установка](#установка)
- [Конфигурация](#конфигурация)
- [Использование](#использование)
- [Функции](#функции)
  - [information_profile()](#information_profile)
  - [get_profile_posts()](#get_profile_posts)
- [Лицензия](#лицензия)

## Установка

Для использования этого проекта необходимо установить Python. Вы можете установить необходимые пакеты с помощью pip:

```bash
pip install -r requirements.txt
```
or 
```bash
pip install instaloader
```

## Конфигурация

Перед запуском скрипта необходимо настроить учетные данные Instagram в файле `config.ini`. Создайте файл `config.ini` в корневом каталоге проекта со следующим содержимым:

```ini
[instaloader]
user = ваш_логин
password = ваш_пароль
```

Замените `ваш_логин` и `ваш_пароль` на ваш логин и пароль от Instagram.

## Использование

1. Откройте файл `main.py`.
2. Раскомментируйте вызовы нужных функций (`information_profile()` или `get_profile_posts()`).
3. Измените переменную `username` на имя пользователя Instagram, данные которого вы хотите спарсить.

Пример:

```python
def main():
    username = 'example_username'  # Замените на имя пользователя Instagram
    profile = instaloader.Profile.from_username(L.context, username)
    print(information_profile(profile))
    print(get_profile_posts(profile))
```

4. Запустите скрипт:

```bash
python main.py
```

## Функции

### `information_profile()`

Эта функция загружает информацию о профиле указанного пользователя Instagram и сохраняет ее в формате JSON и CSV.

**Параметры:**
- `profile` (Profile): Объект профиля Instagram.

**Возвращает:**
- Сообщение, указывающее пути, где сохранены данные профиля.

**Пример:**

```python
def information_profile(profile: Profile) -> dict:
    # Реализация функции
```

### `get_profile_posts()`

Эта функция загружает посты указанного пользователя Instagram и сохраняет информацию о каждом посте в формате JSON.

**Параметры:**
- `profile` (Profile): Объект профиля Instagram.

**Возвращает:**
- Сообщение, указывающее количество скачанных постов.

**Пример:**

```python
def get_profile_posts(profile: Profile) -> None:
    # Реализация функции
```

## Лицензия

Этот проект лицензирован по лицензии MIT. Подробности см. в файле [LICENSE](LICENSE).
