import itertools
list_of_permutations = []

for permut in itertools.permutations(['W', 'W', 'W', 'B', 'B', 'B', ' ']):
    if permut not in list_of_permutations:
        list_of_permutations.append(permut)

for p in list_of_permutations:
    s = ''
    for k in p:
        s+=k
    print(s)