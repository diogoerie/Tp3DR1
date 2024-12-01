x = "recursão"
def inverterstring(s, i=0):
    if i == len(s):
        return ""
    return inverterstring(s, i + 1) + s[i]
stringinvertida = inverterstring(x)
print( stringinvertida)


