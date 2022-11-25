#!/usr/bin/python3
"""Console for the AirBnB Clone project"""
import cmd
import os


class HBNBCommand(cmd.Cmd):
    """Defines the console used to interact the objects"""
    prompt = "(hbnb) "
    def do_quit(self, line) -> bool:
        """Quit command to exit the program"""
        print("Bye")
        return True
    def do_EOF(self, line) -> bool:
        """EOF CLTR-D to exit the program"""
        return True
    def do_clear(self, line) -> None:
        """Clear command to clear screen of console"""
        os.system('clear')

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()