# def solution(string):
#     return string[::-1]

def solution(string):
    str_len = len(string)
    rev_str = ''
    while str_len > 0:
        # print(string[str_len-1])
        rev_str += string[str_len-1]
        str_len -= 1
    return rev_str

# solution('dupa')
# print(solution('dupa'))


def abc():
    x = [*range(1,10,2)]
    print(x)

abc()