#hw6 work

# def bubble_sort(a_list):
#    for pass_num in range(len(a_list) - 1, 0, -1):
#       for i in range(pass_num):
#          if a_list[i] > a_list[i + 1]:
#             temp = a_list[i]
#             a_list[i] = a_list[i + 1]
#             a_list[i + 1] = temp
a_list = [1, 10, 3, 7, 9, 5]
# bubble_sort(a_list)
# print(a_list)

def selection_sort(a_list):
  for fill_slot in range(len(a_list) - 1, 0, -1):
     pos_of_max = 0
     for location in range(1, fill_slot + 1):
        if a_list[location] > a_list[pos_of_max]:
           pos_of_max = location
     temp = a_list[fill_slot]
     a_list[fill_slot] = a_list[pos_of_max]
     a_list[pos_of_max] = temp

selection_sort(a_list)
print(a_list)

# def insertion_sort(a_list):
#   for index in range(1, len(a_list)):
#     current_value = a_list[index]
#     position = index
#     while position > 0 and a_list[position - 1] > current_value:
#        a_list[position] = a_list[position - 1]
#        position = position - 1
#     a_list[position] = current_value
# insertion_sort(a_list)
# print(a_list)