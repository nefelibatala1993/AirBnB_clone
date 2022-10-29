#!/usr/bin/python3
"""Defines the HBNBCommand class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for the AirBnB clone"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """Quit program with EOF (Ctr-D)"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
