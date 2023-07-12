list_num = [2, 17, 44, 14, 99, 21, 37, 22]
add_list = sorted([x for x in list_num if x % 2 == 0])
even_list = sorted([x for x in list_num if x % 2 != 0])
add_list.extend(even_list)
print('Sorted list: ', add_list)
