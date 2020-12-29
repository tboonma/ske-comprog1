name_list = []

def menu_text():
    if name_list:
        return "(N)ew (S)how (D)elete (Q)uit : "
    else:
        return "(N)ew (Q)uit : "

def new_item():
    global name_list
    name = input("Name : ")
    name_list.append(name)
    return f"{name} added"

def show_item():
    for index,name in enumerate(name_list,1):
        print(f"({index}) {name}")
        

def delete_item():
    global name_list
    while True:
        num = input("Number? : ")
        try:
            num = int(num)
        except:
            print("Not a number")
            continue
        if num <= len(name_list) and num > 0:
            break
        else:
            print("Not in range")
    name_list.pop(num-1)
    show_item()

if __name__ == '__main__':
    while True:
        action = input(menu_text()).lower()
        if action == 'n':
            print(new_item())
        elif action == 's' and name_list:
            show_item()
        elif action == 'd' and name_list:
            delete_item()
        elif action == 'q':
            print("Bye")
            break
        else:
            print("Incorrect Menu")
