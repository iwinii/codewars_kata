# def remove_char(s):
#     x = len(s)
#     arr = list(s)
#     arr.pop(0)
#     arr.pop(x-2)
#     return ''.join(arr)

def remove_char(s):
    return s[1:len(s)-1]
print(remove_char('dupa'))
