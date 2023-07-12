from collections import deque

number = int(input('Enter the number: '))
num_list = [1, 2, 3, 4, 5, 6, 7]


def mixing_list(data, num):
    deq_list = deque(num_list)
    for _ in range(number):
        deq_list.appendleft(deq_list.pop())
    return deq_list


new_list = list(mixing_list(num_list, number))
print('Mixed list: ', new_list)

