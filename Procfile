web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn guide_project.wsgi:guide_project -w 2 -b :8000 --timeout 120