chmod +x run
kill -9 PID

## Create admin user
python3 manage.py createsuperuser

## Migrate
python3 manage.py makemigrations <app_name>
python3 manage.py migrate

## Create service
django-admin startproject <service_name>

## Create app
python3 manage.py startapp <app_name>