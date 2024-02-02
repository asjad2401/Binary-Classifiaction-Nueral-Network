def solution(x, y):
    imp = "impossible"
    x =int(x)
    y =int(y)
    count =0

    while(x>1 or  y>1):
        if x>y:
            if x> 10*y:
                multi = (int(x/y) -1)
                count += multi
                x = x - (multi*y)
                continue
            x = x-y
            count+=1
            continue
        elif y>x:
            if y > 10*x:
                multi = (int(y/x) -1)
                count += multi
                y = y - (multi*x)
                continue
            y = y-x
            count+=1
            continue

        if(x==y):
            return imp
        
    return str(count)