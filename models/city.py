#!/usr/bin/python3
"""city module inheriting from the BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class taking city name

    Attributes:
        state_id:(str) it will be the State.id
        name:(str)empty string to take city name
    """
    state_id = ""
    name = ""
