#!/usr/bin/python3
"""Entry point of the command line Interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Entry point of the interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Closes the interpreter\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Do nothing when ENTER key is pressed"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class eg 'create BaseModel'\n"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                obj = eval(f"{arg}()")
                print(obj.id)
                obj.save()
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints an object based on its class name and id
        eg. show BaseModel 123232\n"""
        args = arg.split()
        if (len(args) == 0):
            print("** class name missing **")
        elif (len(args) == 1):
            print("** instance id missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            objects = BaseModel.all()
            id_exists = False

            for key, value in objects.items():
                if args[0] in key:
                    obj_id = key[len(args[0]) + 1:]
                    if args[1] == obj_id:
                        print(value)
                        id_exists = True
                        break

            if not id_exists:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        eg destroy BaseModel 342352"""
        args = arg.split()
        if (len(args) == 0):
            print("** class name missing **")
        elif (len(args) == 1):
            print("** instance id missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            objects = BaseModel.all()
            id_exists = False

            for key, value in objects.items():
                if args[0] in key:
                    obj_id = key[len(args[0]) + 1:]
                    if args[1] == obj_id:
                        del value
                        id_exists = True
                        break

            if not id_exists:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name eg all BaseModel or all"""
        if arg == "" or arg == "BaseModel":
            objects = BaseModel.all()
            obj_list = []

            for key, value in objects.items():
                obj_list.append(value.__str__())

            print(obj_list)
        else:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
