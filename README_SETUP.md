
1. create docker file 
2. create docker-compose file

shell 
    docker-compose run app sh -c "django-admin.py startproject app ."
### mean: run "app service" (docker-compose.yml) in shell mode

include travis to requirements.txt
3. create travis.yml

To_test
    docker-compose run app sh -c "python manage.py test"

    docker-compose run app sh -c "python manage.py test & flake8"






   # NOTE

   