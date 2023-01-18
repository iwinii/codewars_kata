def even_or_odd(number):
    number = int(number)
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


print(even_or_odd(21))
print(even_or_odd(20))
print(even_or_odd(12345))
print(even_or_odd(0))
