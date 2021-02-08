![screenshot](https://i.gyazo.com/0157a4379b728b8c98ee9b3514f7dda7.png)

# xzn.fr

### A minimal URL shortening service made with Django 2.2.

**Requirements:**

- Django v2.2
- pytz v2020.1
- sqlparse v0.3.1

**How to use:**

1. Clone the Github repository:

```bash
git clone [https://github.com/SmithJesko/xzn.fr.git](https://github.com/SmithJesko/xzn.fr.git)
```

2. From the `/src` directory, activate the virtual environment:

```bash
. env/Scripts/activate
```

3. Install requirements:

```bash
pip install -r requirements.txt
```

4. Make database migrations and migrate:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the server:

```bash
python manage.py runserver
```

6. Access the website at `127.0.0.1:8000`