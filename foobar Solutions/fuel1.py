        
from fractions import Fraction
import numpy as np


def replace_probability(m):
    m = np.array(m, dtype=float)
    row_sums = m.sum(axis=1)
    non_zero_rows = row_sums != 0

    m[non_zero_rows] /= row_sums[non_zero_rows, None]
    return m.tolist()

def RQ(m, terminal_state, non_terminal_state):
    m = np.array(m)
    R = m[non_terminal_state][:, terminal_state].tolist()
    Q = m[non_terminal_state][:, non_terminal_state].tolist()
    return R, Q

def subtract_Q_from_identity(Q):
    n = len(Q)
    identity = np.eye(n)
    return (identity - Q).tolist()

def get_minor_matrix(Q, i, j):
    minor_matrix = np.delete(np.delete(Q, i, axis=0), j, axis=1)
    return minor_matrix.tolist()

def get_determinant(Q):
    Q = np.array(Q)
    n = len(Q)

    if n == 1:
        return Q[0, 0]
    if n == 2:
        return np.linalg.det(Q)

    minor_matrices = np.delete(Q, 0, axis=0)[:, 1:]
    determinants = np.array([(-1) ** i * Q[0, i] * get_determinant(minor_matrices[:, :i].tolist() + minor_matrices[:, i+1:].tolist()) for i in range(n)])

    return np.sum(determinants)

def get_transpose_square_matrix(Q):
    return np.transpose(Q).tolist()

def get_inverse(Q):
    Q = np.array(Q)
    n = len(Q)

    Q1 = np.array([((-1) ** (i + j)) * np.linalg.det(get_minor_matrix(Q, i, j)) for i in range(n) for j in range(n)]).reshape((n, n))
    main_determinant = np.linalg.det(Q)
    
    Q1 = np.transpose(Q1) / main_determinant

    return Q1.tolist()

def multiply_matrix(A, B):
    return np.dot(A, B).tolist()

def gcd(a ,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)   

def sanitize(M):
    needed = M[0]
    to_fraction = [Fraction(i).limit_denominator() for i in needed]
    lcm = 1
    for i in to_fraction:
        if i.denominator != 1:
            lcm = i.denominator
    for i in to_fraction:
        if i.denominator != 1:
            lcm = lcm*i.denominator/gcd(lcm, i.denominator)
    to_fraction = [(i*lcm).numerator for i in to_fraction]
    to_fraction.append(lcm)
    return to_fraction

def solution(m):
    n = len(m)
    if n==1:
        if len(m[0]) == 1 and m[0][0] == 0:
            return [1, 1]
    terminal_state = []
    non_terminal_state = []

    
    for row in range(len(m)):
        count = 0
        for item in range(len(m[row])):
            if m[row][item] == 0:
                count += 1
        if count == n:
            terminal_state.append(row)
        else:
            non_terminal_state.append(row)
    
    probabilities = replace_probability(m)
    
    R, Q = RQ(probabilities, terminal_state, non_terminal_state)
    IQ = subtract_Q_from_identity(Q)
    
    IQ1 = get_inverse(IQ)
    product_IQ1_R = multiply_matrix(IQ1, R)
    return sanitize(product_IQ1_R)

