-- settings.sql
CREATE DATABASE my_social;
CREATE USER myuser WITH PASSWORD 'myuser';
GRANT ALL PRIVILEGES ON DATABASE my_social TO myuser;