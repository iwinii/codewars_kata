def test_string_concat(var1, var2):
    return '%f %f' % (var1, var2)

# result = test_string_concat('abc','asd')
result = test_string_concat(1.2,2)

print(result)

def test_string_concat_2(var1, var2):
    return '{1} {0}'.format(var1,var2)

result = test_string_concat_2(1.2,2)

print(result)

def test_string_concat_3(var1, var2):
    return f'{var1} {var2}'

result = test_string_concat_3(1.2,2)

print(result)