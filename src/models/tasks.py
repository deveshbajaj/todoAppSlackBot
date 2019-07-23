from mongoengine import Document, StringField


class Tasks(Document):
    """
    TASK: Create a model for task with minimalists
                    information required for user authentication
    """
    task_details = StringField(max_length=100, required=True)
    channel_id = StringField(max_length=50, required=True)
    user_name = StringField(max_length=50, required=True)