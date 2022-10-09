from itertools import permutations

def perms(object):
    string = str(object)
    perm_set = []    
    perm_list = [''.join(p) for p in permutations(string)]
    for item in perm_list:
        if item not in perm_set:
            perm_set.append(item)
    print(len(perm_set))
    return len(perm_set)

W = input('Enter any String: ')
perms(W)
