def sortedSum(a):
    # Write your code here
    n =int(len(a))
    t =[]
    numbers =[]
    tsum=0
    for i in range(1, n+1):
        numbers.append(i)
        j = 0
        if j < len(t) and t[j] <= a[i-1]:
            j += 1
        t.insert(j, a[i-1])
        tsum += sum(map(lambda x, y: x * y, numbers, t))
        #tsum += sum(numbers*t)
    return tsum % 1000000007

print(sortedSum([9,5,8]))