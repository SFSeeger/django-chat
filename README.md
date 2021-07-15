# Django Chat App
___
## How to Run
___
With docker compose everything you need to run the app will be provided<br />
### Attention: when using docker compose you need to run the command in debug.txt in the mysql container in order to work properly 
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
pytohn manage.py runserver
#If you want to reach the webserver from ouside your local machine use this:
pytohn manage.py runserver 0.0.0.0:8000
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




