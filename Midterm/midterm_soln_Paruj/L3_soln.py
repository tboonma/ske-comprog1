# Level 3 (100)
# 80 for correctness of the solution
# 20 for clarity and style

'''
Implement the following function that returns a list of integer lists. Each integer list element groups the same element(s) from the interger input list, int_list, together.

def group_elements(int_list):


Examples:
print(group_elements([1, 3, 3, 4, 2, 5, 8, 5, 6, 7])) # [[1], [3, 3], [4], [2], [5, 5], [8], [6], [7]]
print(group_elements([3, 3, 3, 3])) # [[3, 3, 3, 3]]
print(group_elements([3, 3, 1, 3, 3, 1])) # [[3, 3, 3, 3], [1, 1]]
print(group_elements([5, 3, 1, 2, 4, 10])) # [[5], [3], [1], [2], [4], [10]]

You do not need to include docstring and doctest for this problem, but your code must pass all the test cases above. Note that the ordering of the groups can be different.
'''
# solution without dictionary
def find_index_list_of_element(e, gl):
    for i in range(len(gl)):
        if e in gl[i]:
            return i
    return -1

def group_elements(int_list):
    group_list = []
    for element in int_list:
        index_list_of_element = find_index_list_of_element(element, group_list)
        if index_list_of_element == -1:
            group_list.append([element])
        else:
            group_list[index_list_of_element].append(element)
    return group_list
'''
# solution using dictionary

def group_elements(int_list):
    d = dict()
    for element in int_list:
        if element not in d:
            d[element] = 1
        else:
            d[element] += 1
    group_list = []
    for key in d:
        group_list.append([key] * d[key])
    return group_list
'''
print(group_elements([1, 3, 3, 4, 2, 5, 8, 5, 6, 7])) # [[1], [3, 3], [4], [2], [5, 5], [8], [6], [7]]
print(group_elements([3, 3, 3, 3])) # [[3, 3, 3, 3]]
print(group_elements([3, 3, 1, 3, 3, 1])) # [[3, 3, 3, 3], [1, 1]]
print(group_elements([5, 3, 1, 2, 4, 10])) # [[5], [3], [1], [2], [4], [10]]
print(group_elements([3, 3, 1, 3, 5, 3, 1, 5, 5, 5, 3, 8, 7, 8])) # [[3, 3, 3, 3, 3], [1, 1], [5, 5, 5, 5], [8, 8], [7]]
