#Missing Number
Mylist = [1, 2, 3, 4, 6, 7, 8, 9, 10]
def findmissingnumber (list, n):
    sum1 = n*(n+1)/2
    sum2 = sum(list)
    print(int(sum2-sum1))


findmissingnumber(Mylist, len(Mylist))
