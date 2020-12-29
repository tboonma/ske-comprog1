# example 1
# num = 0
# count = 0
# while num!= -99:
#     count += 1
#     num = int(input(f"Enter value{count}: "))
# if count - 1 <= 1:
#     print(f"You entered {count - 1} number")
# else:
#     print(f"You entered {count - 1} numbers")

# example 2
# num = 0
# count = 0
# summ = 0
# while num!= -99:
#     count += 1
#     summ += num
#     num = int(input(f"Enter value{count}: "))
# if count - 1 <= 1:
#     print(f"You entered {count - 1} number")
# else:
#     print(f"You entered {count - 1} numbers")
# print(f"Sum of them = {summ}")

# example 3
# num = 0
# count = 0
# mylist = []
# while num!= -99:
#     count += 1
#     num = int(input(f"Enter value{count}: "))
#     mylist.append(num)
# mylist.pop()
# print(mylist)
# avg = sum(mylist)/(len(mylist))
# print(f"{avg:.2f}")

# example 4
# def read_list_while():
#     num = 0
#     mylist = []
#     while num!= -99:
#         num = int(input(f"Enter value{len(mylist)+1}: "))
#         mylist.append(num)
#     mylist.pop()
#     return mylist
# llist1 = read_list_while()
# print(llist1)
# print(f'{sum(llist1)/len(llist1):.2f}')

# example 5
# def read_list_while():
#     num = 0
#     mylist = []
#     while num!= -99:
#         num = int(input(f"Enter value{len(mylist)+1}: "))
#         mylist.append(num)
#     mylist.pop()
#     return mylist
# print("Enter vector 1:")
# llist1 = read_list_while()
# print("Vector 1:")
# print(llist1)
# print("Enter vector 2:")
# llist2 = read_list_while()
# print("Vector 2:")
# print(llist2)

# example 6
def read_list_while():
    num = 0
    mylist = []
    while num!= -99:
        num = int(input(f"Enter value{len(mylist)+1}: "))
        mylist.append(num)
    mylist.pop()
    return mylist
def sum_vector(list1,list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] + list2[i])
    return list3
def diff_vector(list1,list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(abs(list1[i] - list2[i]))
    return list3
def dot_vector(list1,list2):
    dot = 0
    for i in range(len(list1)):
        dot += list1[i] * list2[i]
    return dot
print("Enter vector 1:")
llist1 = read_list_while()
print("Vector 1:")
print(llist1)
print("Enter vector 2:")
llist2 = read_list_while()
print("Vector 2:")
print(llist2)
print(f"Sum result:\n{sum_vector(llist1,llist2)}")
print(f"Diff result:\n{diff_vector(llist1,llist2)}")
print(f"Dot product:\n{dot_vector(llist1,llist2)}")

# example 7
# def print_every_n(list1,n):
#     for i in range(1,len(list1)):
#         if i % n == 0:
#             print(list1[i-1])
# def print_mod_n(list1,n):
#     for i in list1:
#         if i % n == 0:
#             print(i)
# def find_n(list1,n):
#     list2 = []
#     for i in range(len(list1)):
#         if list1[i] == n:
#             list2.append(i)
#     return list2

# v1 = [1,2,3,4,5,6,7,8,9,10,11,12,3,3,9,3,99]
# n = 3
# print('Initial vector:')
# print(v1)
# print(f'Print every {n}th number:')
# print_every_n(v1,n)
# print(f'Print numbers divisible by {n}')
# print_mod_n(v1,n)
# print(f'Print list index of {n}')
# index_result = find_n(v1,n)
# print(index_result)