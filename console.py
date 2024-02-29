#!/usr/bin/python3
"""Console Module"""
import cmd
from models import storage
from models.base_model import BaseModel
import shlex  # for splitting the line into arguments


class HBNBCommand(cmd.Cmd):
    """Interprets commands for the HBNB console"""
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
        """
        Creates a new instance of BaseModel,
        saves it to the JSON file, and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in storage.classes():
            print("** class doesn't exist **")
            return
        new_instance = storage.classes()[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        args = shlex.split(arg)
        if args and args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in storage.all().values() if not args or
               isinstance(obj, storage.classes().get(args[0], object))])

    def do_update(self, arg):
        """
        Updates an instance based on the
        class name and id by adding or updating attribute.
        """
        args = shlex.split(arg)
        if len(args) < 4:
            print("** class name missing **" if len(args) < 1 else
                  "** instance id missing **" if len(args) < 2 else
                  "** attribute name missing **" if len(args) < 3 else
                  "** value missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        key = f"{args[0]}.{args[1]}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        instance = objects[key]
        setattr(instance, args[2], args[3].strip('"'))
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
