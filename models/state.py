#!/usr/bin/python3
"""State module inheriting from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class

    Attribute:
        name: str(empty string-to be filled with
        state name
    """
    name = ""
