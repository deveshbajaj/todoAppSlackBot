import logging
from flask import request
import json
import logging
from services import user_service, spam_service

logger = logging.getLogger("default")


def index():
    """
        This is an introduction function. 
    """
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"


def login():
    """
    Takes username and password from user and calls the login_user function.
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


def search():
    """
        searches for user 
    """
    try:
        data = request.args.to_dict()
        all_user_service = user_service.UserService()
        res = all_user_service.search_user(data)
        return json.dumps(res)
    except Exception as identifier:
        logging.exception(identifier)
        return "500 Internal Server Error"


def view():
    try:
        data = request.args.to_dict()
        all_user_service = user_service.UserService()
        res = all_user_service.view_user(data)
        return json.dumps(res)
    except Exception as identifier:
        logging.exception(identifier)
        return False


def addSpam():
    try:
        data = request.args.to_dict()
        print(data)
        all_spam_service = spam_service.SpamService()
        res = all_spam_service.add_spam(data)
        return json.dumps(res)
    except Exception as identifier:
        logging.exception(identifier)
        return False