from mongoengine import Document, StringField


class UserLogs(Document):
    """
        TASK: Log the user who are logged in
        parameter :
                username :
                id(mongo db id)
                timestamp(time at which the user logged in )
    """
    user_name = StringField(max_length=50, required=True)
    mongo_id = StringField(max_length=50, required=True)
    timestamp = StringField(max_length=50)
