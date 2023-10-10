#!/usr/bin/python3
"""the console program for AirBnB"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand."""

    intro = "Welcome to AirBnB Clone - The console\n"
    prompt = "(hbnb) "

    def emptyline(self):
        """emptyline and enter does nothing anymore"""
        pass

    def do_quit(self, line):
        """Quit: Exit the application.\n"""
        return True

    def do_EOF(self, line):
        """(Ctrl+D): Exit the program."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
