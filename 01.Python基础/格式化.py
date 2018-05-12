import time

print 'name: %s, age: %d' % ('robin', 18)

print 'name: {}, age: {}'.format('robin', 18)

print 'code is %05d' % 1

print 'price is %.2f' % 110.123456

print time.strftime('%Y-%m-%d', time.strptime('2009-12-05', '%Y-%m-%d'))