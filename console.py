#!/usr/bin/python3
"""
This module defines the HBNBCommand class.
It serves as the entry point for the command interpreter for the HBnB project.
"""

import cmd
from models import storage, BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBnB project."""
    prompt = '(hbnb) '
    class_names = ["BaseModel"]

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        "Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()  # Adjust for dynamic class instantiation
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        "Shows the string representation of an instance based on the class name and id."
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        # Implement logic to find instance by id and class name, then print

    def do_destroy(self, arg):
        "Deletes an instance based on the class name and id, saving the change into the JSON file."
        # Similar structure to do_show, but you will delete the instance if found

    def do_all(self, arg):
        "Prints all string representation of all instances based or not on the class name."
        # Implement logic to print all instances, optionally filtered by class name

    def do_update(self, arg):
        "Updates an instance based on the class name and id by adding or updating an attribute."
        # Implement logic to update an instance's attribute, ensuring to handle all error cases

if __name__ == '__main__':
    HBNBCommand().cmdloop()
