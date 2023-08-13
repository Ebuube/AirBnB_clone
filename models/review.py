#!/usr/bin/python3
"""review module inheriting from the BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class

    Attributes:
        place_id:empty(str),it will be the place.id
        user_id:empty(str),it will be the User.id
        test: empty(str)
    """
    place_id = ""
    user_id = ""
    text = ""
