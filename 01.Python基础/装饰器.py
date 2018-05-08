def a(func):
    def inner():
        print 'start'
        func()
        print 'end'
    return inner


@a
def b():
    print 'hello'

    
if __name__ == '__main__':
    b()
