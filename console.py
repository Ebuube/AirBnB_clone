#!/usr/bin/python3
"""
This module defines the console to manage the AirBnB clone project
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    This class specifies the commands available for the console
    """
    prompt = '(hbnb) '

    # COMMANDS

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

    # HELP

    def help_quit(self):
        """
        Provide documentation on the quit command
        """
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
