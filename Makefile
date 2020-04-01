

migrate:
	python manage.py migrate


loaddata:
	python manage.py loaddata ./resources/cards.json


prepdb: migrate loaddata