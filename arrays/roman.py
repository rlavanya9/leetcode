def roman(s): 
 
    val = []
        # out = []
    out = 0
    for element in s:
        if element == 'I':
            val.append(1)
        elif element == 'V':
            val.append(5)
        elif element == 'X':
            val.append(10)
        elif element == 'L':
            val.append(50)
        elif element == 'C':
            val.append(100)
        elif element == 'D':
            val.append(500)
        elif element == 'M':
            val.append(1000)
    # print(val)
    for i in range(len(val)):
        # for j in range(i):
        print(i)
        print(i-1)
        if val[i-1] < val[i]:
            # print(val[i])
            # print(val[i-1])
            out += val[i] - val[i-1]
        else:
            out += val[i]
    return out

print(roman("IV"))