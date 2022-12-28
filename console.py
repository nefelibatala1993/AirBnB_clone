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
        elif line in HBNBCommand.classes.keys():
            new_obj = HBNBCommand.classes[line]()
            storage.save()
            print(new_obj.id)
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
            obj_info = line.partition(" ")
            obj_cls_name = obj_info[0]
            obj_id = obj_info[2]

            if obj_cls_name not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif not obj_id:
                print("** instance id missing **")
            else:
                obj_id = obj_id.partition(" ")[0] # Remove trailing args
                key = obj_cls_name + "." + obj_id
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
                    del(storage.all()[key])
                    storage.save()

    def do_all(self, line) -> None:
        """\n\tPrints all string representation of all instances based or
        not on the class name.

            Syntax: all <class name> or all
        """
        obj_list = []

        if line:
            line = line.split(' ')[0] # Remove any possible trailing args
            if line not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, val in storage.all().items():
                if key.split('.')[0] == line:
                    obj_list.append(str(val))
        else:
            for key, val in storage.all().items():
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
