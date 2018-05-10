class A:
    pass

setattr(A, 'name', 'robin')

print A.name

print getattr(A, 'name')