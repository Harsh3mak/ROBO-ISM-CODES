def mode(l):
    f = 0
    max = 0
    for i in l:
        c = l.count(i)
        if c>f:
            f=c
            max = i
    print(max)
l=[1,2,2,33,3,4,1,1]
print("input ", l)
mode(l)