def fibo_gen(n):
    i = 1
    number = 1
    while i <= n:
        number = number * i
        i += 1
        yield number


def fibonacci():
    i = 1
    number = 1
    while True:
        number = number * i
        i += 1
        yield number


for i in fibo_gen(10):
    print(i)

my_gen = fibonacci()
i = 1
while i < 100:
    print(next(my_gen))
    i += 1
