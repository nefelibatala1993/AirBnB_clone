#!/usr/bin/python3
"""Defines the HBNBCommand class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for AirBnB clone"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Quit the command line with Ctr-D

        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self) -> bool:
        """Overriding the default `empty line + return`"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
