n = int(input("enter: "))

if n % 2 != 0:
    n = 2 * (n // 2)

for i in range(n + 1):
    if i <= n // 2:
        for j in range(1, n + 2):
            if j <= (n // 2 + 1 - i) or j >= (n // 2 + 1 + i):
                print("*", end="")
            else:
                print(" ", end="")
        print()
    else:
        for j in range(1, n + 2):
            if j >= (n // 2 + 1 + (n - i)) or j <= (n // 2 + 1 - (n - i)):
                print("*", end="")
            else:
                print(" ", end="")
        print()