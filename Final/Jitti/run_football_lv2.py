from football import *

ARS = Football("ARS", "Arsenal")
LIV = Football("LIV", "Liverpool")
print(ARS)
print(LIV)

ARS.won(LIV)
print(ARS)
print(LIV)

LIV.drew(ARS)
print(ARS)
print(LIV)

ARS.losed(LIV)
print(ARS)
print(LIV)

print()

CHE = Football("CHE", "Chelsea")
MUN = Football("MUN", "Manchester United")
MCI = Football("MCI", "Manchester City")
print(CHE)
print(MUN)
print(MCI)

MCI.losed(CHE)
print(CHE)
print(MUN)
print(MCI)

MUN.won(MCI)
print(CHE)
print(MUN)
print(MCI)