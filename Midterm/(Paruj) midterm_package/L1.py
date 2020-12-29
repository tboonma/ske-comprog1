# Level 1

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
    """Your docstring goes here; starting with a general description.
    There are six testcases
    Details for arguments, return value, and exceptions go here.

    Your doctests go here
    >>> char_index_list("aabaabaacca", 'a') # [0, 1, 3, 4, 6, 7, 10]
    [0, 1, 3, 4, 6, 7, 10]
    >>> char_index_list("abcdefg", 'b') # [1]
    [1]
    >>> char_index_list("aaaaaccccc", 'a') # [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]
    >>> char_index_list("dkncdddd", 'd') # [0, 4, 5, 6, 7]
    [0, 4, 5, 6, 7]
    >>> char_index_list("helloworld", 'l') # [2, 3, 8]
    [2, 3, 8]
    >>> char_index_list(1234, 4) # Error
    Traceback (most recent call last):
        ...
    TypeError: The two inputs must be string
    """

    # your code goes here
    if not isinstance(s, str) and not isinstance(c, str):
        raise TypeError("The two inputs must be string")
    index = []
    for i in range(len(s)):
        if s[i] == c:
            index.append(i)
    return index

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    