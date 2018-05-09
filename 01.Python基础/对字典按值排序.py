a = [
        {'name': 'zhanfei', 'age': 8},
        {'name': 'mingwei', 'age': 1},
        {'name': 'robin', 'age': 30},
    ]

print a
print sorted(a)
print sorted(a, key=lambda x: x['age'], reverse=True)