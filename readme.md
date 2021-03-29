# nhandzok.herokuapp.com

This is the repo for my projects blog (not including another projects). Feel free to use it for your own site, play around with it etc.

![](https://img.shields.io/badge/Django-3.1.2-green)
![](https://img.shields.io/badge/Python-3.4-green)

Requirements
-------------
All requirements: [requirements.txt](https://github.com/nhantruong2712/blog-fbv/blob/main/requirements.txt)

Quickstart
-------------
Clone the repo and install the requirements
+ Python 3.4
+ Django 3.1.2
`$ pip install django`

Then, copy the settings.py into settings.py and change them as desired.
`$ cp blog/settings.py brobin/settings.py`

Update the database, create a user, and you're good to go!

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

