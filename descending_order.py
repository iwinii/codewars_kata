def descending_order(num):
    arr = [*str(num)]
    arr.sort(reverse=True)
    return int(''.join(arr))

result = descending_order(8639)
print(result)
