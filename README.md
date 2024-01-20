#  Реализация простого API для управления пользователями
### **Задание:**

- Требуется создать простой веб-сервис для управления пользователями. Сервис должен предоставлять API для создания, просмотра и удаления пользователей.


## Подготовка и запуск проекта

#### Шаг 1. Клонируйте репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/user_control.git
```
#### Установка и создание виртуального окружения
- Откройте терминал или командную строку
- Перейдите в каталог, где вы хотите создать виртуальное окружение
- Введите следующую команду:
```python
    python3 -m venv venv
```
- Активация виртуального окружения
```python
Windows:

myenv\Scripts\activate

macOS и Linux:

source myenv/bin/activate


```

#### Шаг 2. Выполняем комманду
```python
    pip install -r requirements.txt
```

#### Шаг 3.Создаем и применяем миграции:
```python
    python manage.py makemigrations
    python manage.py migrate
```

#### Шаг 4.Создать суперюзера
```python
    python manage.py createsuperuser
```
#### Шаг 5 Используя Django Faker заполняем БД
```python
    python manage.py authapp_createdata
```

#### Шаг 6. Запускаем сервер 
```python
    python manage.py runserver
```


## Примеры
Для формирования запросов и ответов использована программа [Postman](https://www.postman.com/).
### Coздание пользователя
```json
POST  http://127.0.0.1:8000/users/create/

{ 
    "email":"test@mail.ru",
    "username":"username"
}
```
### Получаем список юзеров
```json
GET http://127.0.0.1:8000/users/
```

### Получаем детальную информацию о юзере
```json
GET http://127.0.0.1:8000/users/1/
```

### Удаление
```json
DELETE  http://127.0.0.1:8000/delete/1/
```


### Документация по API доступно
```html
http://127.0.0.1:8000/swagger/
```


