def serdup(l):
    for i in l:
        if l.count(i)==2:
            print(i)
            break
l=[]
for i in range(1,100):
    l.append(i)
l.append(4)
print("input", l)
serdup(l)