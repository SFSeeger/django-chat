# Django Chat App
___
## Description
___
As the name already says this is a chat app developed with the backend framework <strong>django</strong>. 
I tried to be as versatile as possible for example using websockets with the <strong>django_channels</strong> package which required me to use redis as signaling and
channel layer manager. For the frontend i first used plain <strong>javascript</strong>, but later switched to <strong>jquery</strong>.
My project heavily relies on <strong>docker</strong> (redis, mysql) so i made it possible to run it all with one docker-compose command. 
Django, relying on the <strong>templating engine</strong>, rendered my usual coding style not really usable for making native frontend applications for django 
(making a frontent in Vue, React or Angular and serving this as static (e.g. like in <strong> Spring Boot, Nest.js, Express.js</strong>) while the backend only serves the data),
so i was forced to use <strong>Axios</strong>, to make kind of 'reactive' requests to the server on the fly without using websockets
## How to Run
___
With docker compose everything you need to run the app will be provided<br />
### Attention: You have to apply migrations to the database over the docker web container
````shell
docker-compose up
````
With docker built you have to provide the databases by yourself more about this in the functionality page 
````shell
docker built -t django-chat .
docker run -p 8000:8000 django-chat 
````
When you don't have docker installed you can use the standard django run command
````shell
python manage.py runserver
#If you want to reach the webserver from outside your local machine use this:
python manage.py runserver 0.0.0.0:8000
````
## Functionality
___
### Structure:
````
│   .gitignore
│   db.sqlite3
│   debug.txt
│   docker-compose.yml
│   Dockerfile
│   manage.py
│   README.md
│   requirements.txt
│
├───backend
│       asgi.py
│       settings.py
│       urls.py
│       wsgi.py
│       __init__.py
│
├───chat
│       admin.py
│       apps.py
│       consumers.py
│       helper.py
│       models.py
│       routing.py
│       tests.py
│       urls.py
│       views.py
│       __init__.py
│
├───friends
│       admin.py
│       apps.py
│       models.py
│       tests.py
│       urls.py
│       views.py
│       __init__.py
│
├───login
│       admin.py
│       apps.py
│       forms.py
│       models.py
│       tests.py
│       urls.py
│       views.py
│       __init__.py
│
└───templates
    │   thanks.html
    │
    ├───chat
    │       chat_page.html
    │
    ├───friends
    │       friends_index.html
    │
    └───login
            login.html
            sign_up.html

````
#### chat:
Handles the main chat feature of the app with websockets and the required routes and database options to make it all work
#### friends:
Friends feature to add and remove friends with all routes and no models
#### login
Handles account management 
### Special Things:
The helper function in chat is there to check for chats
## Requirements
___
### Databases:
- redis (version 5 / latest)
- mysql (latest)
### Packages:
- requirements.txt
### Docker Container/Images:
- mysql
- redis
- python 3.0

### Additional notices
- Using [wait-for-it](https://github.com/vishnubob/wait-for-it)
