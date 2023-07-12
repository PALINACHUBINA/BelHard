from typing import List, Union, Set

type_list = ['11', 'letter', 11.98, 148, {66, 102}, 'moon']


def list_filter(data):
    new_list: List[Union[str, float, int, Set[int]]] = [x for x in type_list if type(x) == str]
    return new_list


filtered_list = list_filter(type_list)
print(filtered_list)
