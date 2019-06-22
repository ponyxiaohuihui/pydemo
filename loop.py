row = 1
while row < 10:
    col = 1
    while col <= row:
        print('{}*{}={}'.format(col, row, row * col), end='\t')
        col = col + 1
    print()
    row = row + 1
for a in '1234567':
    print(a)
list1 = [1, 2, 3, 4, 5, 6, 'b', '1']
for a in list1:
    print(a)
print('list count is ' + str(list1.count('1')))
list2 = [1, 2, 3, 4, 5, 6]
list2.sort(reverse=True)
print('sort list is ' + str(list2))
tup1 = (1, 2, 3)
list3 = list(tup1)
tup1 = tuple(list2)
print('tuple is ' + str(tup1))
dic1 = {'a': 2, 'b': 3}
print(type(dic1.keys()))
