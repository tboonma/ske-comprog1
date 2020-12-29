# 1
def string_interleave(s1, s2):
    """
    DOCTEST START!!!

    >>> string_interleave("abc", "mnopq") # return ’manbocpq'
    'manbocpq'
    >>> string_interleave("mnopq", "abc") # return ’manbocpq’
    'manbocpq'
    >>> string_interleave("Hello", "Sawasdee Thailand") # return ’SHaewlalsodee Thailand’
    'SHaewlalsodee Thailand'
    >>> string_interleave("Mine", "Thai") # return ’TMhianie’
    'TMhianie'
    >>> string_interleave(123, 456)
    Traceback (most recent call last):
        File "/Users/tawaneiei/Desktop/KU/ComProgI/Week7/doctest_ex.py", line 102, in <module>
            print(string_interleave(123,456))
        File "/Users/tawaneiei/Desktop/KU/ComProgI/Week7/doctest_ex.py", line 19, in string_interleave
            raise TypeError("Only strings are allowed")
    TypeError: Only strings are allowed

    """
    if not isinstance(s1, str) and not isinstance(s2, str):
        raise TypeError("Only strings are allowed")
        return 0
    if len(s2) >= len(s1):
        temp = s2
        s2 = s1
        s1 = temp
    istr1 = 0
    istr2 = 0
    s3 = ""
    while True:
        isfinish = 0
        try:
            s3 += s1[istr1]
            istr1 +=1
        except:
            isfinish += 1
        try:
            s3 += s2[istr2]
            istr2 += 1
        except:
            isfinish += 1
        if isfinish == 2:
            break
    return s3

# 2
def selective_sum(n, k):
    """
    DOCTEST START!!!

    >>> selective_sum(3018, 2) # return 11 as 3 and 8 are the 2 largest digits (larger than 0 and 1)
    11
    >>> selective_sum(593796, 3) # return 25 as 9, 9, and 7 are the 3 largest digits
    25
    >>> selective_sum(12345, 10) # return 15 as 10 is larger than the number of digits in 12345
    15
    >>> selective_sum(1234, 0)
    0
    >>> selective_sum("qqq", "www")
    Traceback (most recent call last):
        File "/Users/tawaneiei/Desktop/KU/ComProgI/Week7/doctest_ex.py", line 95, in <module>
            print(selective_sum(x, y))
        File "/Users/tawaneiei/Desktop/KU/ComProgI/Week7/doctest_ex.py", line 59, in selective_sum
            raise TypeError("Only integers are allowed")
    TypeError: Only integers are allowed

    """
    if not isinstance(n, int) and not isinstance(k, int):
        raise TypeError("Only integers are allowed")
        return 0
    n = list(str(n))
    n.sort(reverse=True)
    sum = 0
    for i in range(k):
        try:
            sum += int(n[i])
        except:
            break
    return sum

# 3
def list_intersect(l1, l2):
    """
    DOCTEST START!!!

    >>> list_intersect([1, 2, 1, 3, 4], [1, 2, 2, 3, 4]) # return [1, 2, 3, 4]
    [1, 2, 3, 4]
    >>> list_intersect([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8]) # return [1, 2, 3, 4]
    [1, 2, 3, 4]
    >>> list_intersect([9, 10, 11, 12], [5, 6, 7, 8]) # return []
    []
    >>> list_intersect([9, 10, 11, 12], [5, 6, 9, 10, 7, 8]) # return [9, 10]
    [9, 10]
    >>> list_intersect(123,456) # return []
    Traceback (most recent call last):
        File "/Users/tawaneiei/Desktop/KU/ComProgI/Week7/doctest_ex.py", line 110, in <module>
            print(list_intersect(2,4))
        File "/Users/tawaneiei/Desktop/KU/ComProgI/Week7/doctest_ex.py", line 102, in list_intersect
            raise TypeError("Only lists are allowed")
    TypeError: Only lists are allowed

    """
    if not isinstance(l1, list) and not isinstance(l2, list):
        raise TypeError("Only lists are allowed")
        return 0
    l3 = []
    for i in l1:
        if i in l2 and i not in l3:
            l3.append(i)
    return l3

if __name__ == "__main__":
    import doctest
    doctest.testmod()
