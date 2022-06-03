def calc(x,s,y):
    if s=='+':
        return x+y
    elif s=='-':
        return x-y
    elif s=='*':
        return x*y
    else:
        return x/y

print("input (3,-,6)")
print(calc(3,'-',6))