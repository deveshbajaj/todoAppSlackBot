import hashlib
from models import tasks
import logging
import json
from datetime import datetime


class TaskServices():
    """
    service function for user related business logic
    """

    def add_task(self, my_data):
        try:
            print(my_data)
            new_task = tasks.Tasks(
                task_details=self.geTaskDetailsTodo(my_data),
                channel_id=my_data['channel_id'][0],
                user_name=my_data['user_name'][0],
            ).save()
            return '*'+new_task.task_details+'* is added in the \
                Channel Todo List'
        except Exception as identifier:
            logging.exception(identifier)
            return str(identifier)

    def remove_task(self, my_data):
        taskdetails = self.geTaskDetailsTodo(my_data)
        data = tasks.Tasks.objects(
            task_details=taskdetails,
            channel_id=my_data['channel_id'][0]
        )
        if len(data) == 1:
            for i in data:
                tmp = i.task_details
                i.delete()
            return "%s (Item is removed)" % tmp
        elif len(data) > 1:
            allTask = []
            for i in data:
                allTask.append(i.task_details)
                i.delete()
            tmp = ' , '.join(allTask)
            return(tmp+" all this tasks are removed")
        else:
            return("No Task Found")

    def list_allTask(self, my_data):
        if 'text' not in my_data:
            data = tasks.Tasks.objects(
                channel_id=my_data['channel_id'][0]
            )
            allTask = []
            for i in data:
                allTask.append((i.task_details, i.user_name))
        else:
            taskdetails = self.checkNoArgument(my_data)
            data = tasks.Tasks.objects(
                task_details__contains=taskdetails,
                channel_id=my_data['channel_id'][0]
            )
            allTask = []
            for i in data:
                allTask.append((i.task_details, i.user_name))
        s = ""
        print(allTask)
        for all in allTask:
            s = s + "%s by *%s*" % all + '\n'
        return s

    def checkNoArgument(self, data):
        try:
            text = data['text']
            if len(text) >= 2 and len(text) < 1:
                return ''.join(text)
            elif len(text) == 0:
                return False
            return text[0]

        except Exception as identifier:
            logging.exception(identifier)
            raise Exception("error ocured")

    def geTaskDetailsTodo(self, data):
        try:
            text = data['text']
            if len(text) >= 2 and len(text) < 1:
                raise Exception("incorrect method")
            return text[0]

        except Exception as identifier:
            logging.exception(identifier)
            raise Exception("error ocurred")
