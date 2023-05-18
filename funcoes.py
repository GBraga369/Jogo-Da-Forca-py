def soma (*num):
    total = 0
    for x in num:
        total += x
    return total

def tupla (n1, n):
    return n1 + n

def chute (x,l):
    palavra = ""
    for a in x:
        if a in l:
            palavra += a
        else:
            palavra += "*"
    return palavra

