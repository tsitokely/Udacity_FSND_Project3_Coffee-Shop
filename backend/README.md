# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

#### For Unix based machine (Bash)
```bash
pip install -r requirements.txt
```
#### For Windows (Powershell)
```Powershell
pip install -r .\requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

### Auth0 and configuration
This application uses Auth0 as a third party authentification
#### Setup Auth0
1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Create new API permissions:
   - `get:drinks`
   - `get:drinks-detail`
   - `post:drinks`
   - `patch:drinks`
   - `delete:drinks`
6. Create new roles for:
   - Barista
     - can `get:drinks-detail`
     - can `get:drinks`
   - Manager
     - can perform all actions

#### Setup .env file
Setup the auth0 connection information in the `.env` file inside the `backend/src/auth` directory:
```
# settings
AUTH0_DOMAIN= 
API_AUDIENCE=
```

> Below the description of each environment variable:
> 
> `AUTH0_DOMAIN`: the domain name for auth0
> 
> `API_AUDIENCE`: the API name on auth0
> 

## Running the server

From within the `backend/src` directory first ensure you are working using your created virtual environment.
Each time you open a new terminal session, setup the following environment variables:
#### For Unix based machine (Bash)
```bash
export FLASK_APP=api.py
```
#### For Windows (Powershell)
```Powershell
$env:FLASK_APP="api.py"
```

To run the server, execute:

#### For all types of shell
```shell
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## API documentation
[View the API.md within ./backend for more details.](./API.md)