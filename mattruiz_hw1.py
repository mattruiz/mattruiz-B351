def sort(ls):
    newlist = []
    while ls:
        for x in ls:
            minimum = ls[0]
            if x < minimum:
                minimum = x
            newlist.append(minimum)
            ls.remove(minimum)    
    return newlist

def countWithRecursion(ls, num):
 if not ls:
     return 0
 elif(ls.pop() == num):
     return (1 + (countWithRecursion(ls, num)))
 else:
     return (0 + (countWithRecursion(ls, num)))


def pascals(depth):
    def calcrown(n):
        line = [1]
        for k in range(n):
            line.append(line[k] * (n-k) / (k+1))
        print line
    for x in range(depth):
        calcrown(x)
        
