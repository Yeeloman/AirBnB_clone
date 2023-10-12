#!/usr/bin/python3
"""the console program for AirBnB"""

import cmd
from models.base_model import BaseModel as BM


class HBNBCommand(cmd.Cmd):
    """HBNBCommand."""

    intro = "Welcome to AirBnB Clone - The console\n"
    prompt = "(hbnb) "

    @staticmethod
    def parseLine(line):
        """parses the input line into tokens"""
        return list(line.split())

    def emptyLine(self):
        """emptyline and enter does nothing anymore"""
        pass

    def do_quit(self, line):
        """Quit: Exit the application.\n"""
        return True

    def do_EOF(self, line):
        """(Ctrl+D): Exit the program."""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel"""

        if line == "":
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_bm = BM()
            """dont forget to save it to the JSON file"""
            print(new_bm.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        token = HBNBCommand.parseLine(line)
        if token == []:
            print("** class name missing **")
        elif token[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        elif:
            print("** no instance found **")
        else:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
