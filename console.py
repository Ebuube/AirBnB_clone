#!/usr/bin/python3
"""
This module defines the console to manage the AirBnB clone project
"""
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This class specifies the commands available for the console
    """
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel}

    # COMMANDS

    def do_create(self, line):
        """
        Create a new instance of 'BaseModel'
        Saves it(to the JSON file)
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

        new = BaseModel()
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

    # HELP

    def help_create(self):
        """
        Provide documentation on the 'create' command
        """
        print("Creates a new instance of 'BaseModel'")
        print("Usage:\n\tcreate <class name>")
        print()

    def help_quit(self):
        """
        Provide documentation on the quit command
        """
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
