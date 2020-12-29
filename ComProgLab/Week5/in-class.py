# example 1
# num = 0
# count = 0
# while num!= -99:
#     count += 1
#     num = int(input(f"Enter value{count}: "))
# print(f"You entered {count - 1} numbers")

# example 2
# num = 0
# count = 0
# summ = 0
# while num!= -99:
#     count += 1
#     summ += num
#     num = int(input(f"Enter value{count}: "))
# print(f"You entered {count - 1} numbers")
# print(f"Sum of them = {summ}")

# example 3
# num = 0
# count = 0
# mylist = []
# while num!= -99:
#     count += 1
#     num = int(input(f"Enter value{count}: "))
#     mylist.append(num)
# print(f"You entered {count - 1} numbers")
# mylist.pop()
# print(mylist)
# avg = sum(mylist)/(len(mylist))
# print(avg)

# example 4
# def read_list_while():
#     num = 0
#     mylist = []
#     while num!= -99:
#         num = int(input(f"Enter value{len(mylist)+1}: "))
#         mylist.append(num)
#     mylist.pop()
#     return mylist

# mylist = read_list_while()
# print(mylist)
# avg = sum(mylist)/(len(mylist))
# print(avg)

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