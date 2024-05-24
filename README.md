## Flask Boilerplate

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP

### Descipción

En caso de usar el servicio en python:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ cd <<nombre_ambiente>>
    $ source bin/activate

Arrancar aplicación con servidor Werkzeug:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ python app.py

Arrancer aplicación con servidor GreenUnicorn:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    # Sin logs ni reload
    $ gunicorn app:APP -w 6 -b 0.0.0.0:3000
    # Con logs y reload
    $ gunicorn app:APP -w 6 -b 0.0.0.0:3000 --reload --access-logfile -

### PyLint

    $ pylint <archivo>.py --reports=yes
    $ pylint **/*.py --reports=yes

### OAuth Responses

https://www.googleapis.com/oauth2/v1/userinfo

```
{
    "id": "7891273891273891273",
    "email": "xyz@gmail.com",
    "verified_email": true,
    "name": "alkdjfa asdlfkjasdklf",
    "given_name": "alkdjfa",
    "family_name": "asdlfkjasdklf",
    "picture": "https://lh3.googleusercontent.com/a-/AOh14GhaGAqhpkQfOw3DRemDILu_0aq2eTvfZdkGmRVe",
    "locale": "es"
}
```

### .env

Archivo <b>.env</b>

DB="sqlite:///db/demo.db"
ENV="local"||"server"
MAIL_PORT=465
MAIL_USER="xyz@gmail.com"
MAIL_PASS="asdfas"
MAIL_HOST="smtp.google.com"

### Migraciones

Migraciones con DBMATE - accesos/sqlite3:

    $ npm run dbmate:new <<nombre_de_migracion>>
    $ npm run dbmate:up
    $ npm run dbmate:rollback

### Datos de Colección 'members'

```javascript
$ mongosh
> use atoq
> db.members.insertMany([
    {
        names: "John",
        last_names: "Doe",
        resume: "Experienced software developer with a focus on backend development.",
        image_url: "http://example.com/john_doe.jpg"
    },
    {
        names: "Jane",
        last_names: "Smith",
        resume: "Expert in frontend technologies and UI/UX design.",
        image_url: "http://example.com/jane_smith.jpg"
    },
    {
        names: "Michael",
        last_names: "Johnson",
        resume: "Seasoned database administrator and data analyst.",
        image_url: "http://example.com/michael_johnson.jpg"
    },
    {
        names: "Emily",
        last_names: "Davis",
        resume: "Project manager with extensive experience in agile methodologies.",
        image_url: "http://example.com/emily_davis.jpg"
    }
])
```
---

Fuentes:

+ https://github.com/pepeul1191/flask-boilerplate-v2
+ https://www.pylint.org/#install
+ https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/
+ https://github.com/pepeul1191/python-bottle-boilerplate