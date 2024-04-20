import numpy as np
n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)], dtype=int)
print(arr.T)
print(arr.flatten())


