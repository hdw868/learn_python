from itertools import chain
from itertools import zip_longest

test_list1 = [1, 2, 3, 4, 5]
test_list2 = ['a', 'b', 'c', 'd']


print('zip:')
for i in zip(test_list1, test_list2):
    print(i)

print('zip_longest:')
for i in zip_longest(test_list1, test_list2):
    print(i)

test_str3 = 'AABBCCDD'

print('chain:')
for i in chain(test_list1, test_str3):
    print(i)

print('concatenate:')
for i in test_list1 + test_str3:
    print(i)
