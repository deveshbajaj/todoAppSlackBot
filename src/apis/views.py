import logging
from flask import request
import json
import logging
from services import task_service
import urllib.parse

logger = logging.getLogger("default")


def addTodo():
    """
        add todo item in list
    """
    try:
        raw_data = request.get_data().decode()
        user_data = urllib.parse.parse_qs(raw_data)
        print(user_data, type(user_data))
        all_task_service = task_service.TaskServices()
        res = all_task_service.add_task(user_data)
        return res

    except Exception as identifier:
        logging.exception(identifier)
        return "500 Internal Server Error"


def removeTodo():
    """
            remove todo item from list
    """
    try:
        raw_data = request.get_data().decode()
        user_data = urllib.parse.parse_qs(raw_data)
        print(user_data, type(user_data))
        all_task_service = task_service.TaskServices()
        res = all_task_service.remove_task(user_data)
        return res  # json.dumps(res)
    except Exception as identifier:
        logging.exception(identifier)
        return "500 Internal Server Error"


def listAll():
    """
        List all to do for a a channel
    """
    try:
        raw_data = request.get_data().decode()
        user_data = urllib.parse.parse_qs(raw_data)
        print(user_data, type(user_data))
        all_task_service = task_service.TaskServices()
        res = all_task_service.list_allTask(user_data)
        return res  # json.dumps(res)
    except Exception as identifier:
        logging.exception(identifier)
        return "500 Internal Server Error"
