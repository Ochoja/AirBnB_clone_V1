#!/usr/bin/python3
"""Entry point of the command line Interpreter"""
import cmd


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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
