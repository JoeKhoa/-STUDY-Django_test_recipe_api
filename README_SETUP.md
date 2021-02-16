
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






   # NOTE SKILL PYTHON, DJANGO, ALGO OR CLEAN CODE

   



 
DJANGO

UserModel
    Custom username with email  

setting.py
    declare : AUTH_USER_MODEL
    app used


TestCase 
    self.assertEqual()
    self.assertTrue()

BaseUserManager
    validation_email
    self.normalize_email # may normalize more, plz view form
    user.save(using=self._db)


