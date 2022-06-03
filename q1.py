def ordlist(l,s):
    if s =='asc':
        for i in range(len(l)):
            for j in range(len(l)-i-1):
                if l[j]>l[j+1]:
                    l[j],l[j+1]=l[j+1],l[j]
        return l
    if s=="desc":
        for i in range(len(l)):
            for j in range(len(l)-i-1):
                if l[j]<l[j+1]:
                    l[j],l[j+1]=l[j+1],l[j]
        return l
    else:
        return l

l=[11,3,44,12]
print('test case l=[11,12,3,44],asc')
print(ordlist(l,"asc"))