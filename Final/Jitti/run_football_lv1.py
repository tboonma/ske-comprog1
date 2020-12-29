from football import *

ARS = Football("ARS", "Arsenal")
print(ARS)
ARS.win = 1
print(ARS)
ARS.draw = 4
print(ARS)
ARS.lose = 2
print(ARS)
print(ARS.win)
print(ARS.draw)
print(ARS.lose)
print()

LIV = Football("LIV", "Liverpool", 1, 3, 4)
print(LIV)
LIV.win = 3
print(LIV)
LIV.draw = 1
print(LIV)
LIV.lose = 6
print(LIV)
print(LIV.win)
print(LIV.draw)
print(LIV.lose)
print()