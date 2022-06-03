def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c=1
            break
    if c==0:
        print(n)

n=10
print("input 10")
for j in range(2,n):
    prime(j)
