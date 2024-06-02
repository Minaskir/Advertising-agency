# Advertising agency

Веб-приложение для приема заказов на изготовление рекламы.

## Установка

1. Клонируйте репозиторий на свой локальный компьютер:

```bash
git clone https://github.com/ваш_пользователь/ваш_проект.git
```
2. Перейдите в директорию проекта:
```
cd bd
```
3. Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Примените миграции:
```
python manage.py migrate
```
## Запуск
Для запуска сервера разработки выполните следующую команду:
```
python manage.py runserver
```
После этого ваше приложение будет доступно по адресу http://127.0.0.1:8000/.

## Дополнительные шаги
Для загрузки начальных данных выполните:
```
python manage.py loaddata initial_data.json
```
Измените в файле myproject/settings.py 'NAME', 'USER','PASSWORD' на ваши данные.