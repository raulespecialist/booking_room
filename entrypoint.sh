#!/bin/bash
python core/manage.py migrate
python core/manage.py collectstatic --no-input --clear

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'meloadik@gmail.com', 'TestPass3')" | python core/manage.py shell
echo "from django.contrib.auth.models import Group; Group.objects.create(name='business')" | python core/manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_user('business1', 'business1@example.com', 'TestPass3')" | python core/manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_user('business2', 'business2@example.com', 'TestPass3')" | python core/manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_user('customer1', 'customer1@example.com', 'TestPass3')" | python core/manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_user('customer2', 'customer2@example.com', 'TestPass3')" | python core/manage.py shell
echo "from django.contrib.auth.models import Group, User; groupb=Group.objects.get(name='business');  business1=User.objects.get(username='business1'); business2=User.objects.get(username='business2'); groupb.user_set.add(business1, business2)" | python core/manage.py shell
export DJANGO_SETTINGS_MODULE=core.settings

exec gunicorn -c config/gunicorn/conf.py --bind :8000 --chdir core core.wsgi:application

exec "$@"