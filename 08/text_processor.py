import abc
import sys


class TextProcessor(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def process(self, text):
        pass

    @abc.abstractmethod
    def name(self):
        pass


class Capitalize(TextProcessor):
    def __init__(self):
        super().__init__()
        self._name = "Capitalize"

    def process(self, text):
        return text.capitalize()

    def name(self):
        return self._name


class ToUpper(TextProcessor):
    def __init__(self):
        super().__init__()
        self._name = "ToUpper"

    def process(self, text):
        return text.upper()

    def name(self):
        return self._name


class ToLower(TextProcessor):
    def __init__(self):
        super().__init__()
        self._name = "ToLower"

    def process(self, text):
        return text.lower()

    def name(self):
        return self._name


processors = {}
for my_class in TextProcessor.__subclasses__():
    processors[my_class().name()] = my_class()

while True:
    my_input = input()
    for i in range(1, len(sys.argv)):
        my_input=processors[sys.argv[i]].process(my_input)
    print(my_input)
