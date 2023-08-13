#!/usr/bin/python3
"""
Variables to be shared via models
"""
from  models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
