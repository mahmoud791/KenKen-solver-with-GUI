import csp
from solver import *
from itertools import product, permutations
from functools import reduce
from random import  random, shuffle, randint, choice






def operation(operator):
    
    if operator == '+':
        return lambda a, b: a + b
    elif operator == '-':
        return lambda a, b: a - b
    elif operator == 'x':
        return lambda a, b: a * b
    elif operator == '÷':
        return lambda a, b: a / b
    else:
        return None

def adjacent(xy1, xy2):
    """
    Checks wheither two positions represented in 2D coordinates are adjacent
    """
    x1, y1 = xy1
    x2, y2 = xy2

    dx, dy = x1 - x2, y1 - y2

    return (dx == 0 and abs(dy) == 1) or (dy == 0 and abs(dx) == 1)

  
  
def conflicting(A, a, B, b):
    
    for i in range(len(A)):
        for j in range(len(B)):
            mA = A[i]
            mB = B[j]

            ma = a[i]
            mb = b[j]
            if ((mA[0] == mB[0]) != (mA[1] == mB[1])) and ma == mb:
                return True

    return False
