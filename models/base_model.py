#!/usr/env/python3
from datetime import datetime
import uuid
"""clase BaseModel"""


class BaseModel:
    """class BaseModel"""
    def __init__(self, *args, **kwargs):
        """__init__ function"""
        if len(kwargs) > 0:
            self.id = kwargs["id"]
            vl = kwargs["created_at"]
            self.created_at = datetime.strptime(vl, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the updated_at to the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
