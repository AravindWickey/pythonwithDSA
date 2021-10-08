# DECIMAL TO BINARY

def dectobi (a):
    return a % 2
    return dectobi(a/2)


print(dectobi(13))