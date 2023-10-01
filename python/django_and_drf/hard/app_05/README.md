# DJANGO APP_05
## Instructions and Navigations

### Software
 Python | Linux | JavaScript  | PostgreSQL  | Django  | React  | Docker

## ERRORS

## Maybe 
After creating the `UserManager` and `User` models, if the migration fails with the following error:<br>
`Migration admin.0001_initial is applied before its dependency core_user.0001_initial on database 'default'.`

Please try running these commands:<br> 
`$ sudo su postgres`<br>
`$  psql`<br>
`postgres=# DROP DATABASE app_05db;`<br>
`postgres=# CREATE DATABASE app_05db;`<br>
`postgres=# ALTER ROLE app_05 SET client_encoding TO 'utf8';`<br>
`postgres=# ALTER ROLE app_05 SET default_transaction_isolation TO 'read committed';`<br>
`postgres=# ALTER ROLE app_05 SET timezone TO 'UTC';`<br>
`postgres=# ALTER DATABASE app_05db OWNER TO app_05;`<br>
`postgres=# GRANT ALL PRIVILEGES ON DATABASE app_05db TO app_05;`<br>

If you already  ran the "makemigrations" for core_user, simply  run `python manage.py migrate`

# Maybe

Insomnia -> if this app dont correct work use alternative -> Postman/curl/etc...
