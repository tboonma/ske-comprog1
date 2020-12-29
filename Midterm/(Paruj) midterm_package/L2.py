# Level 2

'''
Implement the following function that returns a new string that replaces the first occurrence of pattern1 in the input string, s, with pattern2.

def replace_first_occurrence(s, pattern1, pattern2):

Examples:
print(replace_first_occurrence('good bad good bad', 'bad', 'good')) # good good good bad
print(replace_first_occurrence('good good good good', 'bad', 'good')) # good good good good
print(replace_first_occurrence('aaaaa aaa', 'aa', 'zxz')) # zxzaaa aaa
print(replace_first_occurrence('bbab baa', 'aa', 'zxz')) # bbab bzxz
print(replace_first_occurrence('bbaaabbaaaabcccaa', 'aa', 'zxz')) # bzxzabbaaaabcccaa

You do not need to include docstring and doctest for this problem, but your code must pass all the test cases above. 
'''

def replace_first_occurrence(s, pattern1, pattern2):

    # your code goes here; remove the keyword pass below once completed.
    return s.replace(pattern1,pattern2, 1)

print(replace_first_occurrence('good bad good bad', 'bad', 'good'))
print(replace_first_occurrence('good good good good', 'bad', 'good'))
print(replace_first_occurrence('aaaaa aaa', 'aa', 'zxz'))
print(replace_first_occurrence('bbab baa', 'aa', 'zxz'))
print(replace_first_occurrence('bbaaabbaaaabcccaa', 'aa', 'zxz'))
print()

'''
Implement the following function that creates a new list that removes adjacent duplicates from the input integer list, int_list.

def remove_adjacent_duplicates(int_list):

Examples:
print(remove_adjacent_duplicates([1, 1, 1, 1, 2, 5, 5, 5, 3])) # [1, 2, 5, 3]
print(remove_adjacent_duplicates([1, 1, 5, 5, 10, 8, 7, 5, 5, 5, 12, 4, 12, 12])) # [1, 5, 10, 8, 7, 5, 12, 4, 12]
print(remove_adjacent_duplicates([12, 12, 12])) # [12]
print(remove_adjacent_duplicates([1, 2, 3])) # [1, 2, 3]
print(remove_adjacent_duplicates([])) # []

You do not need to include docstring and doctest for this problem, but your code must pass all the test cases above.
'''
def remove_adjacent_duplicates(int_list):

    # your code goes here; remove the keyword pass below once completed.
    finished_list = []
    temp_index = 0
    for i in int_list:
        if temp_index == 0:
            finished_list.append(i)
            temp_index += 1
        elif i != finished_list[temp_index-1]:
            finished_list.append(i)
            temp_index += 1
    return finished_list

print(remove_adjacent_duplicates([1, 1, 5, 5, 10, 8, 7, 5, 5, 5, 12, 4, 12, 12]))
print(remove_adjacent_duplicates([1, 1, 1, 1, 2, 5, 5, 5, 3]))
print(remove_adjacent_duplicates([12, 12, 12]))
print(remove_adjacent_duplicates([1, 2, 3]))
print(remove_adjacent_duplicates([]))
print()

