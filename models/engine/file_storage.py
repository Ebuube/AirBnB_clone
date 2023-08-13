#!/usr/bin/python3
"""The file storage module"""
import json


class FileStorage:
    """class storage that serializes instances
    to a JSON file and deserializes JSON to instances
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initialize some instance specific variables
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        # This list will be updated and the imports to
        # As we keep adding more classes
        self.__classes = {
                            "BaseModel": BaseModel,
                            "User": User,
                            "Place": Place,
                            "State": State,
                            "Amenity": Amenity,
                            "Review": Review}

    def all(self):
        """returns the __objects dict"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key
        <obj class name>.id"""
        key = "{0}.{1}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serilizes the __objects to a JSON file(path:__file_path"""
        s_obj = {}
        for key, obj in self.__objects.items():
            s_obj[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(s_obj, f)

    def reload(self):
        """deserializes the json file to __objects(only if JSON file
        (file__path)exists;otherwise,do nothing.If the file doesn't
        exist,no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as f:
                ds_obj = json.load(f)
                for key, value in ds_obj.items():
                    class_name = key.split('.')[0]
                    cls = self.__classes[class_name]    # changed
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
