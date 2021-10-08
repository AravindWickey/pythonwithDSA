#pair of two sum

def findpairofsum (Mylist, n):
    for i in range (len(Mylist)):
        for j in range (len(Mylist)):
            if Mylist[i] + Mylist[j] == n:
                print(i,j)


list = [2,3,4,5,6]
findpairofsum(list, 7)



