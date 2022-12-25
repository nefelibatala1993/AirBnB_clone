#!/usr/bin/python3
"""Command-line tool for the AirBnB clone"""
import cmd
import os


class HBNBCommand(cmd.Cmd):
    """Command-line tool to help with the AirBnB clone website"""
    def __init__(self) -> None:
        """Instantiation Method / Default Constructor"""
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    # The custom commands below are for the operation of the console
    def do_quit(self, line) -> bool:
        """\n\tQuit command to exit the program\n"""
        return True

    def do_EOF(self, line) -> None:
        """\n\tEOF (ctrl + D) to exit the program\n"""
        return True

    def emptyline(self) -> bool:
        """Method called when an empty line is entered in response
        to the prompt. Here I have overridden in to do nothing if called"""
        pass

    def do_clear(self, line) -> None:
        """\n\tClears the console\n"""
        os.system('clear')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
