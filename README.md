# MomsPops API

## For developers:

#### Аgreements:
- default .env file: .dev.env (in ./src);
- default database: Postgres;
- default requirements file: "requirements.txt";
- unit tests folders: "tests" folder in each app with "test_model.py" and "test_view.py";
- model managers: custom manager should be extra attributes;
You can change it in settings.

#### Applications:
- _core_: project root app;
- _api_: api application;

- users
- coordinates
- locations
- notifications
- profiles
- chat
- reactions


#### Environ variables example:
".dev.env" file in ./src:
```dotenv
SECRET_KEY=secret_SECRET

DB_NAME=mosmpops_example
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
```
#### Linter:

We use `flake8`.
```commandline
flake8
```

#### Type-checker:

We use `mypy`
```commandline
mypy .
```

#### PRs:
IMPORTANT! You should check your code by linter and type-checker before making pull-request.

## Installing requirements
```commandline
pip install -r requirements.txt
```

## Running application
```commandline
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


## Database schema
https://lucid.app/lucidchart/736ac949-7e84-4be3-96b2-25e91ec53ec8/edit?beaconFlowId=C39989B530A6D57F&invitationId=inv_c894ff77-5e97-4e8d-823f-0ffeb53dc3c7&page=0_0#