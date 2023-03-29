chmod +x run
kill -9 PID

## Create admin user
python3 manage.py createsuperuser

## Migrate
python3 manage.py makemigrations <app_name>
python3 manage.py migrate

