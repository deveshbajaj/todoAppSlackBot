from mongoengine import Document, StringField, IntField


class Spam(Document):
    """
        Spam user Collection as the other user adds the any other user as
        Spam , it can be use by other user to check which user is spam
    """
    phoneNo = StringField(max_length=10, required=True)
    count = IntField()
    # from count we can detect what level of spam it is 