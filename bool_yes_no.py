# def bool_to_word(boolean):
#     if boolean == True:
#         return('Yes')
#     else: return ('No')

def bool_and_int_to_word(value):
    if value == True or value == 1:
        return('Yes')
    if value == False or value == 0:
        return ('No')

    return value

print(bool_and_int_to_word(True))
print(bool_and_int_to_word(0))
print(bool_and_int_to_word(1))
print(bool_and_int_to_word(False))
print(bool_and_int_to_word(3))