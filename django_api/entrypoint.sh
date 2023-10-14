#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    # если база еще не запущена
    echo "DB not yet run..."

    # Проверяем доступность хоста и порта
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "DB did run."
fi
# Удаляем все старые данные
echo "Applying migrations"
python manage.py makemigrations movies

python manage.py migrate --fake-initial
python manage.py collectstatic --no-input --clear
python manage.py createsuperuser --noinput

echo "Generate translations"
python manage.py compilemessages --locale ru -v 0
exec "$@"