import numpy
n, m, p = map(int, input().split())
array_1 = numpy.array([list(map(int, input().split())) for _ in range(n)], dtype=int)
array_2 = arr = numpy.array([list(map(int, input().split())) for _ in range(m)], dtype=int)
print(numpy.concatenate((array_1, array_2), axis=0))
