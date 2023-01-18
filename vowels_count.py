def get_count(sentence):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    i = 0
    for x in sentence:
        if x in vowel_list:
            i += 1
    return i

result = get_count('aeiuoy')
print(result)
