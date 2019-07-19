import hashlib
from models import spam
import logging
import json
from datetime import datetime


class SpamService():
    """
    service function for spam related business logic
    """

    def add_spam(self, spam_data):
        """
            TASKS: write the logic here for add spam  in collection
            and increment the counter
        """
        try:

            data = spam.Spam.objects(
                phoneNo=spam_data['phoneNo'])
            if len(data) == 0:
                new_user = spam.Spam(
                    phoneNo=spam_data['phoneNo'],
                    count=0
                ).save()
                return "Spam added"
            else:
                res = self.updateSpam(spam_data)
                if res:
                    return "Spam updated"
                else:
                    return "Spam added failed"
                # return {"res": "User_not_Found"}
        except Exception as identifier:
            logging.exception(identifier)

    def updateSpam(self, spam_data):
        try:
            
            data = spam.Spam.objects(
                phoneNo=spam_data['phoneNo'])
            count = json.loads(data[0].to_json())
            print(count, type(count))
            tmp = count['count']+1
            
            data = spam.Spam.objects(
                phoneNo=spam_data['phoneNo']).update_one(count=tmp)
            return True
        except Exception as identifier:
            logging.exception(identifier)
            return False