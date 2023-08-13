#!/usr/bin/python3
"""
This module defines the console to manage the AirBnB clone project
"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class specifies the commands available for the console
    """
    prompt = '(hbnb) '
    classes = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review}

    # COMMANDS

    def do_update(self, line):
        """
        Update an instance based on the 'class name' and 'id'
        by adding or updating attribute
        """
        args = HBNBCommand.split_str(line)

        if len(args) > 0:
            class_name = args[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        try:
            arg_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return

        obj_key = HBNBCommand.make_key(class_name, arg_id)

        # Search for obj_key in non-empty storage
        try:
            obj = storage.all()[obj_key]
        except KeyError:
            print("** no instance found **")
            return

        # Ensure attribute name and value are present
        try:
            attr = args[2]
        except IndexError:
            print("** attribute name missing **")
            return
        try:
            val = args[3]
        except IndexError:
            print("** value missing **")
            return

        # Cast value to the required type
        # The order must be respected
        """
        if val == int(val):
            val = int(val)
        if val == float(val):
            val = float(val)
        """
        try:
            test = float(val)
            if test == int(test):
                val = int(test)
            else:
                val = test
        except ValueError:
            pass

        # Update the instance
        setattr(obj, attr, val)
        obj.save()

    def do_all(self, line):
        """
        Print all string representation of all instances
        based or not on the class name.
        """
        args = HBNBCommand.split_str(line)

        objs = list()
        if len(args) > 0:
            class_name = args[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            if storage.all() is not None:
                for value in storage.all().values():
                    if value.__class__.__name__ == class_name:
                        objs.append(str(value))

        else:
            if storage.all() is not None:
                for value in storage.all().values():
                    objs.append(str(value))

        print(objs)

    def do_destroy(self, line):
        """
        Delete an instance base on class name and id
        Save the change to storage
        """
        args = HBNBCommand.split_str(line)

        if len(args) > 0:
            class_name = args[0]
        else:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        try:
            arg_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return

        obj_key = HBNBCommand.make_key(class_name, arg_id)

        # Search for obj_key in non-empty storage
        if (not storage.all()) or (obj_key not in storage.all()):
            print("** no instance found **")
            return
        else:
            instance = (storage.all()).pop(obj_key)
            del instance
            storage.save()

    def do_show(self, line):
        """
        Print the string representation of an instance
        based on the class name and id
        """
        args = HBNBCommand.split_str(line)

        if len(args) > 0:
            class_name = args[0]
        else:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        try:
            arg_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return

        obj_key = HBNBCommand.make_key(class_name, arg_id)

        # Search for obj_key in non-empty storage
        if (not storage.all()) or (obj_key not in storage.all()):
            print("** no instance found **")
            return
        else:
            print((storage.all())[obj_key])

    def do_create(self, line):
        """
        Create a new instance of 'BaseModel'
        Saves it to storage
        Prints the id
        """
        args = HBNBCommand.split_str(line)

        if len(args) > 0:
            class_name = args[0]
        else:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        #   new = BaseModel()
        new = HBNBCommand.classes[class_name]()
        new.save()
        print(new.id)

    def do_quit(self, line):
        """
        Quit command to exit the program
        Usage:
        ======
        quit

        Example:
        ========
            (hbnb) quit
        """
        return True

    def do_EOF(self, line):
        """
        End of File to signal exit to the program
        Usage:
        ======
        * EOF
        * <CTRL + D>

        Example:
        ========
            (hbnb) EOF
            (hbnb) <CTRL + D>
        """
        print()
        return True

    # SPECIAL COMMANDS

    def emptyline(self):
        """
        This method defines what happens when an empty line is entered
        at command line
        """
        pass

    @staticmethod
    def split_str(string):
        """
        Split a string into a list
        """
        args = shlex.split(string, posix=True, comments=False)
        return args

    @staticmethod
    def make_key(cls_name, obj_id):
        """
        Create a storage engine key from a class name and object id
        """
        delim = '.'

        return str(cls_name + delim + obj_id)

    # HELP

    def help_update(self):
        """
        Provide documentation on the 'update' command
        """
        print("Update an instance based on class name and id by adding or \
updating attributes")
        print("Usage: update <class name> <id> <attribute> <value>")
        print()

    def help_all(self):
        """
        Provide documentation on the 'all' command
        """
        print("Print all string representation of all instances based or not \
on the class name")
        print("Usage:\n\tall [<class name>]")
        print()

    def help_destroy(self):
        """
        Provide documentation on the 'destroy' command
        """
        print("Delete an instance based on the class name and id")
        print("Usage:\n\tdestroy <class name> <id>")
        print()

    def help_show(self):
        """
        Provide documentation on the 'show' command
        """
        print("Print the string representation of an instance based on \
the class name and id")
        print("Usage:\n\tshow <class name> <id>")
        print()

    def help_create(self):
        """
        Provide documentation on the 'create' command
        """
        print("Create a new instance of 'BaseModel'")
        print("Usage:\n\tcreate <class name>")
        print()

    def help_quit(self):
        """
        Provide documentation on the quit command
        """
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """
        Provide documentation on the EOF command
        """
        print("End of File to signal exit to the program")
        print("Usage:")
        print("\t* EOF")
        print("\t* <CTRL + D>")
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
