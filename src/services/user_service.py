import hashlib
from models import user
import logging
import json
from datetime import datetime


class UserService():
    """
    service function for user related business logic
    """

    def login_user(self, login_data):
        """
            TASKS: write the logic here for user login
                authenticate user credentials as per your
                schema and return the identifier user.

                raise appropriate errors wherever necessary
        """
        try:
            password = hashlib.md5(login_data['password'].encode()).hexdigest()
            data = user.User.objects(
                user_name=login_data['user_name'], password=password)
            if len(data) > 0:
                users = []
                for i_users in data:
                    users.append(i_users.to_json())
                # self.log_logged_user(users)
                return {'user': users}
                # create a session of the and hold the info of users activity
            else:
                return {"res": "User_not_Found"}
        except Exception as identifier:
            logging.exception(identifier)

    def create_user(self, user_data):
        """ 
            task to Create a User in the mongoDb 
        """
        data = user.User.objects(phoneNo=user_data['phoneNo'])
        if len(data) > 0:
            return{
                'res': "User already Exist"
            }
        else:
            password = hashlib.md5(user_data['password'].encode()).hexdigest()
            new_user = user.User(
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                user_name=user_data['user_name'],
                password=password,
                phoneNo=user_data['phoneNo']
            ).save()
            return new_user.to_json()

    def search_user(self, searchData):
        if 'phoneNumbers' in searchData:
            data = user.User.objects(
                phoneNo=searchData['phoneNumbers'])
            if len(data) > 0:
                users = []
                for i_users in data:
                    users.append(i_users.to_json())
                return {'user': users}
            else:
                return {"res": "User_not_Found"}
        elif 'name' in searchData:
            data = user.User.objects(
                user_name=searchData['name'])
            if len(data) > 0:
                users = []
                for i_users in data:
                    users.append(i_users.to_json())
                return {'user': users}
            else:
                return {"res": "User_not_Found"}
        else:
            return "query String Not found"

    def view_user(self, view_data):
        try:
            data = user.User.objects(
                phoneNo=view_data['phoneNumbers'])
            if len(data) > 0:
                users = []
                for i_users in data:
                    users.append(i_users.to_json())
                return {'user': users}
            else:
                return {"res": "User_not_Found"}
        except Exception as identifier:
            logging.exception(identifier)
            return False