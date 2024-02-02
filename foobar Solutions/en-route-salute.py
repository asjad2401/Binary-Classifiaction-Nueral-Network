def solution(s):
    x = len(s)
    inter =0
    for i in range (0,x):
        if s[i] == '>':
            for j in range(i,x):
                if s[j] == '<':
                    inter+=1
            s[i] == '-'
    return 2*inter
              