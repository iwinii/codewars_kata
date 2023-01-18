def test_map(var):
    result = map(multiply, var)
    return list(result)

def multiply(x):
    return x*2

print(test_map([1,2,3]))
