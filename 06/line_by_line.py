import sys


def line_by_line(files):
    for i in range(0, len(files)):
        with open(files[i]) as f:
            for line in f:
                my_input = input()
                if my_input == "q":
                    sys.exit(0)
                if my_input == "n":
                    break
                else:
                    print(line, end="")


line_by_line(sys.argv[1:])

