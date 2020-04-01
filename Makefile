

migrate:
	python manage.py migrate


loaddata:
	python manage.py loaddata ./resources/cloud.json
	python manage.py loaddata ./resources/s3.json


prepdb: migrate loaddata