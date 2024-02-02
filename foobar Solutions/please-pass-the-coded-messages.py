def solution(l):
    l = sorted(l)
    length = len(l)
    if (length==0):
        return 0
    if (length==1):
        if (l[0]%3 ==0):
            return l[0]
        else:
            return 0
    sum =0
    checksum=0
    for i in range(len(l)):
        checksum += l[i]
        sum = sum + (l[i]*pow(10,i))
    if (sum%3 ==0):
        return(sum)
    else:
        for j in range(length):
            if ((checksum-l[j])%3==0):
                newList = l[:]
                del newList[j]
                return solution(newList)
        for j in range(length):
            newList = l[:]
            del newList[j]
            return solution(newList)
        return 0
        
