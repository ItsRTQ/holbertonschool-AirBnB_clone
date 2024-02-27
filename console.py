#!/usr/bin/python3
"""
This module defines the HBNBCommand class.
It serves as the entry point for the command interpreter for the HBnB project.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBnB project."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
