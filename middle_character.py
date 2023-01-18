def get_middle(s):
    dlug = len(s)
    if dlug % 2 == 0:
        mid = int(dlug / 2)
        return s[mid - 1] + s[mid]

    mid = dlug / 2
    mid = int(mid + 0.5)
    return s[mid - 1]


result = get_middle('dupaa')
print(result)
