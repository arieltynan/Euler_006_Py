# Euler Problem 006
# Solved January 2021

# Sum square difference

import math

i = 1
sumsquare = 0
totsum = 0
while i < 101:
    sumsquare = sumsquare + i*i 
    totsum = totsum + i
    i = i + 1

squaresum = totsum*totsum

dif = squaresum - sumsquare
# print(squaresum)
# print(sumsquare)
print(dif)