def my_range(*args):
    if len(args) == 1:
        step = 1
        position = 0
        limit = args[0]
    elif len(args) == 2:
        step = 1
        position = args[0]
        limit = args[1]
    elif len(args) == 3:
        position = args[0]
        limit = args[1]
        step = args[2]
    else:
        return "error"
    while position < limit:
        yield position
        position += step


for i in my_range(10):
    print(i)

for i in my_range(2, 10):
    print(i)

for i in my_range(2, 100, 5):
    print(i)
