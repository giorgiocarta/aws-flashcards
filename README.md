# This is WIP Repo

## Done:

1. Generic AWS Cards questions
2. S3 cards (almost done)

## To do:
1. Ec2
2. etc.
3. etc.

# AWS Flashcards

Simple django website providing a collection of flashcards to practice for the aws associate certification exam.

You can add more flashcard by adding to the json files located into the resources folder. 

Enjoy.

## Installation
```bash
git clone git@github.com:donedeal-giorgio/aws-flashcards.git
cd  cd aws-falshcards
# create virtual env
python3 -m venv .venv

# activate it
source ./.venv/bin/python

# install requirements
pip install -e .
```

## Start the app with

Only the first time:
```bash
python manage.py migrate
python manage.py loaddata ./resources/cloud.json
python manage.py loaddata ./resources/s3.json
python manage.py loaddata ./resources/ec2.json
etc.
```

Start the app with:
```
python manage.py runserver
```

Open the browser at http://0.0.0.0:8080

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


