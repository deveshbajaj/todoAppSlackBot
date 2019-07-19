from mongoengine import Document, StringField


class User(Document):
    """
    TASK: Create a model for user with minimalists
                    information required for user authentication

    HINT: Do not store password as is.
    """
    email = StringField(
        regex="^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$", required=True)
    user_name = StringField(max_length=50, required=True)
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50)
    password = StringField(max_length=50, required=True)
    phoneNo = StringField(max_length=10, required=True)
