def sum(s):
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
    return sum
print("input 'as12e4r' ")
print(sum('as12e4r'))
