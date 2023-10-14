#!/usr/bin/python3
"""the console program for AirBnB"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import json

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter.

        Attributes:
            prompt (str): The command prompt.
    """

    prompt = "(hbnb)"

    @staticmethod
    def parseLine(line):
        """parses the input line into tokens

        :param line: the arguments of the command.
        """
        return list(line.split())

    def emptyLine(self):
        """emptyline and enter does nothing anymore"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """(Ctrl+D): Exit the program."""
        print("")
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel

        Usage: create <Class_name> <Class_id>
        """

        if not line:
            print("** class name missing **")
        elif line in classes.keys():
            new_cls = classes[line]()
            new_cls.save()
            print(new_cls.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance

        Usage: show <Class_name> <Class_id>
        """
        token = HBNBCommand.parseLine(line)
        obj_dic = storage.all()
        if token == []:
            print("** class name missing **")
        elif token[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        elif f"{token[0]}.{token[1]}" not in obj_dic:
            print("** no instance found **")
        else:
            print(obj_dic["{}.{}".format(token[0], token[1])])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id

        Usage: destroy <Class_name> <Class_id>
        """
        token = HBNBCommand.parseLine(line)
        obj_dic = storage.all()
        if token == []:
            print("** class name missing **")
        elif token[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        elif f"{token[0]}.{token[1]}" not in obj_dic:
            print("** no instance found **")
        else:
            dest_cls = f"{token[0]}.{token[1]}"
            for key in obj_dic.keys():
                if dest_cls == key:
                    break
            del obj_dic[dest_cls]
            storage.save()

    def do_all(self, line):
        """do_all.
            Prints all string representation of all\
instances based or not on the class name

        Usage: all <Class_name(optional)>
        """
        all_dic = []
        obj_dic = storage.all()
        token = HBNBCommand.parseLine(line)
        if len(token) > 0 and token[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(token) > 0 and token[0] in classes.keys():
            for obj in obj_dic.values():
                if token[0] == obj.__class__.__name__:
                    all_dic.append(obj.__str__())
            print(all_dic)
        else:
            for obj in obj_dic.values():
                all_dic.append(obj.__str__())
            print(all_dic)

    def do_update(self, line):
        """Updates an instance based on the class name and id

        Usage: Update <Class_name> <Class_id> <attribute> <value>
        """
        token = HBNBCommand.parseLine(line)
        obj_dic = storage.all()
        if token == []:
            print("** class name missing **")
        elif token[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        elif f"{token[0]}.{token[1]}" not in obj_dic:
            print("** no instance found **")
        elif len(token) == 2:
            print("** attribute name missing **")
        elif len(token) == 3:
            print("** value missing **")
        else:
            update_dic = obj_dic["{}.{}".format(token[0], token[1])]
            attrtype = type(update_dic.__dict__[token[2]])
            setattr(update_dic, token[2], attrtype(token[3]))
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
