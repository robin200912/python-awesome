# encoding=utf-8
import time

start = time.time()
a = range(100000000)
print type(a)
end = time.time()
print end - start  # 3.60325598717

# xrange则不会直接生成一个list，而是每次调用返回其中的一个值
# 所以xrange做循环的性能比range好，尤其是返回很大的时候。尽量用xrange吧，除非你是要返回一个列表
start = time.time()
b = xrange(100000000)
print type(b)
end = time.time()
print end - start  # 1.4066696167e-05