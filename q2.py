def crednum(s):
    a = ""
    for i in range(len(s)):
        if i<(len(s)-4):
            a = a+'*'
        else:
            a = a + s[i]
    return a
print("input 123412341234")
print(crednum("123412341234"))