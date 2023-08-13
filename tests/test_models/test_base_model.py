#!/usr/bin/python3
"""
Test for ``BaseModel`` class
"""
import unittest
import os
import pep8
import json
import datetime
from models.base_model import BaseModel
from tests import config


class test_BaseModel(unittest.TestCase):
    """
    Definition of tests for the class
    """
    # Set maxDiff to see all output on error comparison
    maxDiff = None

    def __init__(self, *args, **kwargs):
        """
        Initialize the test instance
        """
        super().__init__(*args, **kwargs)
        self.value = BaseModel
        self.name = self.value.__name__

    def setUp(self):
        """
        Set up the environment for each test method
        """
        # Remove previous storage files
        json_fmt = ".json"
        path = "./"     # path to work on

        for root, dirs, files in os.walk(path):
            for _file in files:
                if _file.endswith(json_fmt):
                    file_path = os.path.join(root, _file)
                    os.remove(file_path)
                    if config.setUp_verbose is True:
                        print("Removed: '{}'".format(file_path))

    def tearDown(self):
        """
        Tear down method for each test
        """
        # Remove previous storage files
        json_fmt = ".json"
        path = "./"     # path to work on

        for root, dirs, files in os.walk(path):
            for _file in files:
                if _file.endswith(json_fmt):
                    file_path = os.path.join(root, _file)
                    os.remove(file_path)
                    if config.setUp_verbose is True:
                        print("Removed: '{}'".format(file_path))

    def test_check_pep8_compliance(self):
        """
        Ensure all '*.py' files are pep8 (or pycodestyle) compliant
        It is ran only ``once`` during a test
        """
        if config.pep8_checked is False:
            path = "./"
            style = pep8.StyleGuide(quite=False, show_source=True,
                                    verbose=config.pep8_verbose)
            result = style.check_files(paths=path)
            self.assertEqual(result.total_errors, 0, "Fix pep8")
            config.pep8_checked = True

    def test_BaseModel_id(self):
        """
        Ensure that ``BaseModel.id`` is implemented
        """
        # id is of right type
        foo = BaseModel()
        self.assertTrue(hasattr(foo, 'id'))
        self.assertTrue(type(foo.id), str)

        # Each instance has a different id
        bar = BaseModel()
        self.assertNotEqual(foo.id, bar.id)

    def test_BaseModel_created_at(self):
        """
        Ensure that ``BaseModel.id`` is implemented
        """
        # created_at attribute is of right type
        foo = BaseModel()
        self.assertTrue(hasattr(foo, 'created_at'))
        self.assertTrue(type(foo.created_at), datetime)

    def test_BaseModel_updated_at(self):
        """
        Ensure that ``BaseModel.id`` is implemented
        """
        # updated_at attribute is of right type
        foo = BaseModel()
        self.assertTrue(hasattr(foo, 'updated_at'))
        self.assertTrue(type(foo.updated_at), datetime)

        # It should be updated every time an object is saved
        prev = foo.updated_at
        foo.save()
        self.assertNotEqual(foo.updated_at, prev)
