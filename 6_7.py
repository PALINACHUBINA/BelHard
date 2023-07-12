number_list = [1, 3, 5, 6, 10]
sum_list = []

left_index = -1
right_index = -len(number_list) + 1
middle_index = 0
while middle_index < len(number_list):
    sum_list.append(number_list[left_index] + number_list[right_index])
    left_index += 1
    right_index += 1
    middle_index += 1

print(sum_list)
