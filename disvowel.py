def disemvowel(string):
    return ''.join([x for x in string if x not in 'aeiouAEIOU'])


print(disemvowel('ala ma kotA'))
