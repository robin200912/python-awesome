# example 1
def a():
    x, y = 1, 2
    return x, y

x, y = a()
print x, y

# example 2
x, y, _, _ = (1, 2, 3, 4)
print x, y


# example 3
def b(*args, **kwargs):
    print args
    print kwargs

b(1, 2, a=1, b=2)