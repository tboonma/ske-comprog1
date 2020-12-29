# Level 3

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

def group_elements(int_list):

    # your code goes here; remove the keyword pass below once completed.
    int_added = []
    group = []
    for i in int_list:
        if i not in int_added:
            temp = []
            for j in range(int_list.count(i)):
                temp.append(i)
            group.append(temp)
            int_added.append(i)
    return group
            

print(group_elements([1, 3, 3, 4, 2, 5, 8, 5, 6, 7])) # [[1], [3, 3], [4], [2], [5, 5], [8], [6], [7]]
print(group_elements([3, 3, 3, 3])) # [[3, 3, 3, 3]]
print(group_elements([3, 3, 1, 3, 3, 1])) # [[3, 3, 3, 3], [1, 1]]
print(group_elements([5, 3, 1, 2, 4, 10])) # [[5], [3], [1], [2], [4], [10]]
