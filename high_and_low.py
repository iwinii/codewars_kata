def high_and_low(numbers):
    num = numbers.split()
    print(num)
    hnum = int(num[0])
    lnum = int(num[0])
    for i in num:
        i = int(i)
        if i > hnum:
            hnum = i
        if i < lnum:
            lnum = i
    return ''+str(hnum)+' '+str(lnum)

result = high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4')
print(result)

def high_and_low_2(numbers):
    num = numbers.split()
    list = []
    for i in num:
        list.append(int(i))
    return str(max(list))+' '+str(min(list))

result = high_and_low_2('8 3 -5 42 -1 0 0 -9 4 7 4 -4')
print(result)