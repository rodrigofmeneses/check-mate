# CheckMate API

## *Be the king of your organization and checkmate your tasks.*

![CheckMate](assets/be_the_king_white.jpg)

This Project is a collaborative work to developer a full stack TODO list APP. This repository contains the backend part of project what will be integration with Web and Mobile by @Joninhas @Fabrício.

---

**Technologies used:** 

The mainly technologies used are:
* Python
* FastAPI

For database model and migrations:
* SQLModel
* Alembic

Check it out `requirements.in` and `requirements-dev.txt` for the majors Python and FastAPI dependencies to development.

Last and not least
* Docker 
* PostgreSQL

---
**Configuration:**

This project is design to be container first, so after cloning the respository:

```
docker-compose up
```
In other terminal, execute to apply migrations:
```
docker-compose exec api alembic upgrade head
```

If you opt for non docker developer environment, follow these steps:

1. Create a virtual environment and install all dependencies:

```
# Create virtual environment and activate
python -m venv .venv
source .venv/bin/activate # Linux
.venv/script/activate # Windows

# Install dependencies
pip install -r requirements-dev.txt
pip install -e . # Install the project to use CLI
```

2. Setup Database, copy `postgres/create-databases.sh` to `/docker-entrypoint-initdb.d/` folder in your system and restart your PostgreSQL to create a database in initalization. 

3. Configure environment variables in `checkmate/default.toml` or `.env` if prefer.

4. Run project:
```
uvicorn todo.app:app --host=0.0.0.0 --port=8000 --reload
```
---

**Usage**

Access `http://localhost:8000/docs` or `http://localhost:8000/redoc` to visualize the project documentation.

You can interact with swagger and test the routes.

<!-- If you want to test using a rest client, you can click the button below:

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)]()

**Here's my project deployed to** -->