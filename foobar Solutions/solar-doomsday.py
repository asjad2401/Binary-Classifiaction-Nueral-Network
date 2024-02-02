import math
def solution(area):
    output =[]
    while(area>0):
        sq = (int)(math.sqrt(area))
        output.append(sq)
        area = area - sq
            
    print(output)
solution(12)