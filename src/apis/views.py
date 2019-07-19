import logging
from flask import request
import json
import logging
from services import user_service

logger = logging.getLogger("default")


def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"


def login():
    """
                TASKS: write the logic here to parse a json request
                and send the parsed parameters to the appropriate service.
                return a json response and an appropriate status code.
                Sending data to API by raw Data from Postman :  
    """
    try:
        raw_user_data = request.get_data().decode()
        login_data = json.loads(raw_user_data)
        all_user_service = user_service.UserService()
        res = all_user_service.login_user(login_data)
        return json.dumps(res)
    except Exception as identifier:
        logging.exception(identifier)
        return "500 Internal Server Error"


def create():
    """
            Creates a New user in MongoDb
    """
    try:
        raw_user_data = request.get_data().decode()
        user_data = json.loads(raw_user_data)
        print(user_data, type(user_data))
        all_user_service = user_service.UserService()
        res = all_user_service.create_user(user_data)
        return json.dumps(res)
    except Exception as identifier:
        logging.exception(identifier)
        return "500 Internal Server Error"
