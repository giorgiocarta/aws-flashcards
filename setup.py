from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='aws-flashcards',
	version='0.0.3',
	packages=[''],
	url='https://github.com/donedeal-giorgio/aws-flashcards.git',
	license='MIT',
	author='Giorgio Carta',
	install_requires=[
		"asgiref==3.2.3",
		"Django==3.1.12",
		"django-crispy-forms==1.8.1",
		"django-environ==0.4.5",
		"django-fsm==2.7.0",
		"django-fsm-admin==1.2.4",
		"Pillow==7.0.0",
		"pytz==2019.3",
		"sqlparse==0.3.0",
		"psycopg2==2.8.4"
	],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: POSIX :: Linux",
		"Development Status :: 3 - Alpha",
		"Framework :: Django",
		"Intended Audience :: Education"
	],
	author_email='giorgiocarta@gmail.com',
	description='A flashcards collection for aws associate certificate exam',
	long_description=long_description,
	long_description_content_type="text/markdown",
)
