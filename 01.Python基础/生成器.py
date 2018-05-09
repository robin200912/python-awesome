# example1
g1 = (i for i in range(1, 11))
print type(g1)


# example2
def a():
    for i in range(1, 11):
        yield i

g2 = a()
print type(g2)
for b in g2:
    print b