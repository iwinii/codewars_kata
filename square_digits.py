def square_digits(num):
    num_str = str(num)
    output = ''
    for x in num_str:
        x = int(x)
        output += str(x*x)
    return output

result = square_digits(123456)
print(result)
