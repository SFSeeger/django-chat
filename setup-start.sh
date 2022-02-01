python manage.py makemigrations
echo "makemigrations"
python manage.py migrate --run-syncdb
echo "migrate"
python manage.py runserver 0.0.0.0:8000
echo "run"