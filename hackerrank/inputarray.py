import numpy
n, m = map(int, input().split())
arr = numpy.empty((n, m), dtype=int)
for i in range(n):
    arr[i] = numpy.array(list(map(int, input().split())))


# m = numpy.array([list(map(int, input().split())) for _ in range(n)],dtype=int)