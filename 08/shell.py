import abc
import sys


class Command(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def help(self):
        pass

    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def exec(*args):
        pass


class PrintArgs(Command):
    def __init__(self):
        super().__init__()

    def name(self):
        return "print"

    def help(self):
        return "Prints its arguments"

    def exec(self, args):
        for arg in args:
            print(arg)


class Quit(Command):
    def __init__(self):
        super().__init__()

    def name(self):
        return "q"

    def help(self):
        return "terminates shell"

    def exec(self, args):
        sys.exit(0)


commands = {}
for my_class in Command.__subclasses__():
    commands[my_class().name()] = my_class()

while True:
    command = input()
    if command == "help":
        for my_class in commands:
            print(commands[my_class].name() + ":", commands[my_class].help())
    else:
        parts = command.split()
        commands[parts[0]].exec(parts[1:])