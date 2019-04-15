def my_map(function, args):
    results = []
    for arg in args:
        results.append(function(arg))
    return results


def reverse(arg):
    return arg[::-1]


print(my_map(reverse, ["one", "two", "three"]))
