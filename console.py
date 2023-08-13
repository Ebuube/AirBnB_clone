#!/usr/bin/python3
"""
This module defines the console to manage the AirBnB clone project
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class specifies the commands available for the console
    """
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel}

    # COMMANDS

    def do_all(self, line):
        """
        Print all string representation of all instances
        based or not on the class name.
        """
        args = HBNBCommand.split_str(line)

        objs = list()
        if len(args[0]) > 0:
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

        if len(args[0]) > 0:
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

        #   obj_key = class_name + arg_id
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

        if len(args[0]) > 0:
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

        #   obj_key = class_name + '.' + arg_id
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

        if len(args[0]) > 0:
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
        delim = ' '     # whitespace as delimiter
        return string.split(sep=delim)

    @staticmethod
    def make_key(cls_name, obj_id):
        """
        Create a storage engine key from a class name and object id
        """
        delim = '.'

        return str(cls_name + delim + obj_id)

    # HELP

    def help_all(self):
        """
        Provide documentation on the 'all' command
        """
        print("Print all string representation of all instances")
        print("based or not on the class name")
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
        print("Print the string representation of an instance")
        print("based on the class name and id")
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
