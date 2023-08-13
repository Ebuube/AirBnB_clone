#!/usr/bin/python3
"""amenity module inheriting from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class taking name of amenity

    Attribute:
        name: (str)Name of Amenity
    """
    name = ""
