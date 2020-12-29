
# Level 1 (100)
# 50 for correctness of the solution
# 50 for clarity and completeness of docstring and doctest

'''
Implement the following function that returns the list of indices of a specified character,c, in an input string, s.

def char_index_list(s, c):

Include Google’s style docstring and put at least six normal test cases in the doctest. In addition, your code needs to raise appropriate exceptions and  exception test cases needs to be included in the doctest as well.

Examples:
print(char_index_list("aabaabaacca", 'a')) # [0, 1, 3, 4, 6, 7, 10]
print(char_index_list("aabaabaacca", 'b')) # [2, 5]
print(char_index_list("aabaabaacca", 'c')) # [8, 9]
print(char_index_list("aabaabaacca", 'e')) # []
'''

def char_index_list(s, c):
    """Find index positions of a given character, c, in an input string, s

    Args:
        s (string): input string
        c (string): input character (string of length 1)

    Returns:
        (list): a list of indices indicating the positions of the input character, c, in the input string, s
    
    Raises:
        TypeError: if s and c are not string
        ValueError: if c is not a string of length 1

    Examples:
    >>> char_index_list("aabaabaaccadede", 'a')
    [0, 1, 3, 4, 6, 7, 10]
    >>> char_index_list("aabaabaaccadede", 'b')
    [2, 5]
    >>> char_index_list("aabaabaaccadede", 'c')
    [8, 9]
    >>> char_index_list("aabaabaaccadede", 'd')
    [11, 13]
    >>> char_index_list("aabaabaaccadede", 'e')
    [12, 14]
    >>> char_index_list("aabaabaaccadede", 'f')
    []
    >>> char_index_list(8092.78, '2')
    Traceback (most recent call last):
        ...
    TypeError: 8092.78 or 2 is not a string

    >>> char_index_list("aabaabaaccadede", 'abcd')
    Traceback (most recent call last):
        ...
    ValueError: abcd is not a string of length one

    """

    if isinstance(s, str) == False or isinstance(c, str) == False:
        raise TypeError('{} or {} is not a string'.format(s, c))
    if len(c) != 1:
        raise ValueError('{} is not a string of length one'.format(c))

    temp_list = []
    for index, element in enumerate(s):
        if element == c:
            temp_list.append(index)
    return temp_list

