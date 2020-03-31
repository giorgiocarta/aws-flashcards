# AWS Flashcards

Simple django website providing a collection of flashcards to practice for the aws associate certification exam.

You can add more flashcard by adding to the json files located into the resources folder. 

Enjoy.

## Installation
```bash
git clone github@...  
cd  ...
python3 -m venv .venv

```

## Start the app with

```bash
python manage.py migrate
python manage.py loaddata ./resources/s3.json
python manage.py runserver
```

## Run with docker

```bash
docker-compose up --build 
```

## env file example

To run with the a local sqllite database, set DB_SETUP equals to `local`, and
that's the only env variable required. 

When running using docker-compose, you'll need the following env
 variables can use the following settings
```
DEBUG=
DB_SETUP=postgres
POSTGRES_PASSWORD=django_password
POSTGRES_USER=django_user
POSTGRES_DB=django_cards
POSTGRES_HOST=db
ALLOW_IP_RANGE=0.0.0.0/0
```


