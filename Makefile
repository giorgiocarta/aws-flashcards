

migrate:
	python manage.py migrate


loaddata:
	python manage.py loaddata ./resources/category.json
	python manage.py loaddata ./resources/cloud.json
	python manage.py loaddata ./resources/s3.json
	python manage.py loaddata ./resources/ec2.json

prepdb: migrate loaddata