#!/usr/bin/python3
"""Command-line tool for the AirBnB clone"""
import cmd
import os
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command-line tool to help with the AirBnB clone website"""
    classes = {
        'BaseModel': BaseModel
    }

    prompt = '(hbnb) '

    def do_create(self, line) -> None:
        """\n\tCreates a new instance based on the specified class name.\n
        After creating the new instance it will be stored in the JSON
        file, and the id will be printed to the stdout.

            Syntax: create <class name>
        """
        if not line:
            print("** class name missing **")
        elif (line in HBNBCommand.classes.keys()):
            new_obj = eval(line)()
            storage.save()
            print(f"{new_obj.id}")
        else:
            print("** class doesn't exist **")

    def do_show(self, line) -> None:
        """\n\tPrints the string representation of an instance based on the class
        name and id

            Syntax: show <class name> <id>
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line) -> None:
        """\n\tDeletes an instance based on the class name and id.\n
        After deleting the instance, the changes will be saved to the
        JSON file.

            Syntax: destroy <class name> <id>
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all().keys():
                    print("** no instance found**")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line) -> None:
        """\n\tPrints all string representation of all instances based or
        not on the class name.

            Syntax: all <class name> or all
        """
        if not line:
            obj_list_all = [
                str(val) for val in storage.all().values()
            ]
            print(obj_list_all)
        else:
            if line not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            else:
                obj_list = []
                for val in storage.all().values():
                    if val.to_dict()['__class__'] == line:
                        obj_list.append(str(val))
                print(obj_list)

    def do_update(self, line) -> None:
        """Updates an instance based on the class name and id by adding
        or updating attribute.\n
        After the attribute of the instance is updated, the changes will
        be saved to the JSON file.

            Syntax: update <class name> <id> <attribute name> <attribute value>
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all().keys():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** attribute value missing")
                else:
                    obj = storage.all()[key]
                    setattr(obj, args[2], args[3].strip('\"'))
                    storage.save()

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
