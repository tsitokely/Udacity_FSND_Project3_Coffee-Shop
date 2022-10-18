from logging import raiseExceptions
import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

#db_drop_and_create_all()

# ROUTES
'''
@OK implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route("/drinks")
def retrieve_drinks():
    try:
        all_drinks = Drink.query.all()

        return jsonify(
            {
                    "success": True,
                    "drinks": [drink.short() for drink in all_drinks]
            }
            )
    except:
        abort(500)


'''
@OK implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route("/drinks-detail")
@requires_auth('get:drinks-detail')
def retrieve_drinks_details(jwt):
    try:
        all_drinks = Drink.query.all()

        return jsonify(
            {
                    "success": True,
                    "drinks": [drink.long() for drink in all_drinks]
            }
            )
    except:
        abort(500)


'''
@OK implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route("/drinks", methods=["POST"])
@requires_auth('post:drinks')

def create_drink(json):
    body = request.get_json()

    new_title = body.get("title", None)
    new_recipe = str('"')+str(body.get("recipe", None))+str('"') #TODO - change during front end implementation

    try:
        new_drink = Drink(
        title = new_title,
        recipe = new_recipe
                    )
        print(new_title)
        new_drink.insert()

        return jsonify(
            {
                "success": True,
                "created": new_drink.id,
                "drinks": new_drink.long(),
            }
        )
    except Exception as e:
        print(e)
        abort(422)

'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''


# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@OK implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''
@app.errorhandler(400)
def bad_request(error):
    return jsonify(
        {
            "success": False,
            "error": 400,
            "message": "bad request"
        }
        ), 400

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify(
        {
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }
        ), 405

@app.errorhandler(422)
def unprocessable(error):
    return jsonify(
        {
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }
        ), 422

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "There was an issue with the server. Please contact the administrator"
    }), 500
'''
@OK implement error handler for 404
    error handler should conform to general task above
'''
@app.errorhandler(404)
def not_found(error):
    return jsonify(
        {
            "success": False,
            "error": 404,
            "message": "resource not found"
        }
        ), 404

'''
@OK implement error handler for AuthError
    error handler should conform to general task above
'''
@app.errorhandler(AuthError)
def unprocessable(error):
    return jsonify({
            'Error type': 'Authentification error',
            'description': 'Your request has authorization issues',
            'Authorization error status': str(error.status_code),
            'Authorization error code': str(error.error['code']),
            'Authorization error desc': str(error.error['description'])
        })
