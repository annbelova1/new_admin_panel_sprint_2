FROM python:3.8.6-alpine

# рабочая директория внутри проекта
WORKDIR /usr/src/django_api

# переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgre
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .


# chmod 774 django_api/entrypoint.sh
RUN ["chmod", "+x", "/usr/src/django_api/entrypoint.sh"]

ENTRYPOINT ["/usr/src/django_api/entrypoint.sh"]

