DROP DATABASE  if exists django_cards;

CREATE DATABASE django_cards;

CREATE USER django_user WITH PASSWORD 'django_password';

ALTER ROLE django_user SET client_encoding TO 'utf8';
ALTER ROLE django_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE django_cards TO django_user;
