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

    def test_magic_str(self):
        """
        Ensure that the `__str__` method is implemented
        """
        foo = BaseModel()
        expected_str = "[{}] ({}) {}".format(type(foo).__name__, foo.id,
                                             foo.__dict__)

        self.assertEqual(str(foo), expected_str)

    def test_save(self):
        """
        Ensure that the ``save`` method is implemented
        It updates the public instance attribute `updated_at` with
        current datetime
        """
        foo = BaseModel()
        self.assertTrue(hasattr(foo, 'save'))
        prev = foo.updated_at
        foo.save()
        new = datetime.datetime.now()
        self.assertTrue(new >= foo.updated_at and foo.updated_at > prev)

    def test_to_dict(self):
        """
        Ensure that the ``to_dict`` method is implemented
        It returns a dictionary a dictionary containing all keys/values
        of `__dict__`
        """
        foo = BaseModel()
        self.assertTrue(hasattr(foo, 'to_dict'))

        dic = foo.to_dict()
        # Ensure `__class__` name is the name of the class of the object
        self.assertTrue(hasattr(dic, '__class__'))
        self.assertEqual(dic['__class__'], type(foo).__name__)

        # 'created_at' and 'updated_at' attributes must be converted to strings
        # format: %Y-%m-%dT%H:%M:%S.%f
        fmt = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)

        time_attrs = ['created_at', 'updated_at']
        for key in time_attrs:
            with self.subTest(key=key):
                self.assertEqual(type(dic[key]), str)
                self.assertEqual(dic[key], getattr(foo, key).isoformat())
