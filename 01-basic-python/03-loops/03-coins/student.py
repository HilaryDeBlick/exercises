from operator import truediv
from pickle import TRUE


def coins(one, two, five, goal):
    for x in range(one+1):
        for y in range(two+1):
            for z in range(five+1):
                if x + 2*y + 5*z == goal:
                    return True
    return False