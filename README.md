# Платформа электронного обучения

Для запуска проекта установите зависимости из файла:
```
requirements.txt
```

### Разработка моделей для системы управления контентом
### Разработка системы управления контентом
### Кеширование содержимого проекта

Для получения Docker-образа Memcached:
```
docker pull memcached:1.6.26
```

Запуск Docker-контейнера Memcached:
```
docker run -it --rm --name memcached -p 11211:11211 memcached:1.6.26 -m 64
```

### Разработка RESTful API

#### Примеры запросов к API:

Получить список всех курсов (GET):
```
http://127.0.0.1:8000/api/courses/
```

Получить определенный курс (GET):
```
http://127.0.0.1:8000/api/courses/1/
```

Зачисление пользователя на курс (POST):

(Требуется аутентификация)
```
http://127.0.0.1:8000/api/courses/<pk>/enroll/
```

### Разработка чат-сервера проекта

Запуск Docker-контейнера Redis для установки канального слоя:
```
docker run -it --rm --name redis -p 6379:6379 redis:7.2.4
```
