def g1(x):
    yield range(x)


def g2(x):
    yield from range(x)   # python 3


it1 = g1(5)
it2 = g2(5)

print(type(it1))
print(type(it2))

print([x for x in it1])
# out [range(0, 5)]
print([x for x in it2])
# out [0, 1, 2, 3, 4]
