# Level 2 (100)
# 80 for correctness of the solution
# 20 for clarity and style

'''
Implement the following function that returns a new string that replaces the first occurrence of pattern1 in the input string, s, with pattern2.

def replace_first_occurrence(s, pattern1, pattern2):

Examples:
print(replace_first_occurrence('good bad good bad', 'bad', 'good')) # good good good bad
print(replace_first_occurrence('good good good good', 'bad', 'good')) # good good good good
print(replace_first_occurrence('aaaaa aaa', 'aa', 'zxz')) # zxzaaa aaa
print(replace_first_occurrence('bbab baa', 'aa', 'zxz')) # bbab bzxz
print(replace_first_occurrence('bbaaabbaaaabcccaa', 'aa', 'zxz')) # bbzxzabbaaaabcccaa

You do not need to include docstring and doctest for this problem, but your code must pass all the test cases above. 
'''

def replace_first_occurrence(s, pattern1, pattern2):

    pattern1_index = s.find(pattern1)
    if pattern1_index != -1:
        new_string = s[0:pattern1_index] + pattern2 + s[pattern1_index + len(pattern1):]
        return new_string
    else:
        return s

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

    if len(int_list) == 0:
        return []
    new_list = []
    prev_element = int_list[0]
    for element in int_list[1:]:
        if element != prev_element:
            new_list.append(prev_element)
        prev_element = element
    new_list.append(prev_element)
    return new_list

print(remove_adjacent_duplicates([1, 1, 5, 5, 10, 8, 7, 5, 5, 5, 12, 4, 12, 12]))
print(remove_adjacent_duplicates([1, 1, 1, 1, 2, 5, 5, 5, 3]))
print(remove_adjacent_duplicates([12, 12, 12]))
print(remove_adjacent_duplicates([1, 2, 3]))
print(remove_adjacent_duplicates([]))
print()
