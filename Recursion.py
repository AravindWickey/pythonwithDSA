# fibonacci Number
def fibonacci(n):
    assert n>=0 and int(n) == n, 'not a rightttt inputttt'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(-3))