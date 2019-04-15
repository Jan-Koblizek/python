import sys
import time


class Logger:
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._level = 0
        self._printers = []

    def set_level(self, level):
        self._level = level

    def log(self, level, message):
        if level > self._level:
            for p in self._printers:
                p.print(message)

    def add_printer(self, printer):
        self._printers.append(printer)


class PrinterStd:
    def __init__(self):
        super().__init__()

    def print(self, message):
        print(message)


class PrinterErr:
    def __init__(self):
        super().__init__()

    def print(self, message):
        sys.stderr.write(message)


class PrinterFile:
    def __init__(self, file):
        super().__init__()
        self._file = file

    def print(self, message):
        with open(self._file, "w+") as f:
            f.write(message)


class FormatterTime():
    def format(self, my_logger, message):
        return time.asctime(time.localtime(time.time())) + ", " + my_logger._name + ", " + message


logger = Logger("Logger1")
std_print = PrinterStd()
err_print = PrinterErr()
file_print = PrinterFile("test.txt")
logger.add_printer(std_print)
logger.add_printer(err_print)
logger.add_printer(file_print)
formatter = FormatterTime()
logger.log(2, formatter.format(logger, "testing"))
