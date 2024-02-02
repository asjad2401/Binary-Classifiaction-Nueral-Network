
def solution(pegs):
    n = len(pegs)
    numerator = pegs[1] - pegs[0]
    denominator = 1
    min_even = numerator
    max_odd = 0

    for i in range(2, n):
        if i % 2 == 0:
            numerator += -(pegs[i] - pegs[i - 1])
            if numerator > max_odd:
                max_odd = numerator
        else:
            numerator += pegs[i] - pegs[i - 1]
            if numerator < min_even:
                min_even = numerator

    numerator *= 2
    if n % 2 == 0:
        if numerator % 3 == 0:
            numerator /= 3
        else:
            denominator = 3

    if numerator < (max_odd + 1) * denominator or numerator > (min_even - 1) * denominator:
        numerator = denominator = -1

    return [int(numerator), int(denominator)]
