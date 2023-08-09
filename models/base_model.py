#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
# The variable 'storage' was used but I don't think it has been created


class BaseModel:
    """
    A base model class that defines all the common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        args:handle variable number of arguments
        id : generation of unique id on every instance created
        created_at: the datetime that the object was created
        updated_at: the datetime updates anytime any info in the
                     object is updated
        """
        if kwargs:
                        for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                        )
                else:
                    setattr(self, key, value)
        else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self):
        """
        representation of objects as stings
        it should print:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ([]) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Always save the datetime anytime updated_at is
        updated
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        return a dictionary containing all the key/values
        of ___dict__ od the instance
        """
        dic_of_obj = self.__dict__.copy
        dic_of_obj["__class__"] == type(self).__name__
        dic_of_obj["created_at"] == self.created_at.isoformat()
        dic_of_obj["updated_at"] == self.update_at.isoformat()
        return dic_of_obj
