#!/usr/bin/python3
""" Console Module """
import cmd
from models import storage
from models.base_model import BaseModel
import shlex  # for splitting the line into arguments

class HBNBCommand(cmd.Cmd):
    """ Interprets commands for the HBNB console """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id, saving the change into the JSON file."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        args = shlex.split(arg)
        objects = storage.all()
        if len(args) > 0 and args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in objects.items() if not arg or key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in objects:
            print("** no instance found **")
            return
        instance = objects[key]
        if args[2] not in ['id', 'created_at', 'updated_at']:
            setattr(instance, args[2], args[3].strip('"'))
            instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
