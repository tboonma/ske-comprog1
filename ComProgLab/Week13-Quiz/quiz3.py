class Device:
    def __init__(self, name, watt, status):
        self.__name = name
        self.__watt = watt
        self.__status = status

    def __str__(self):
        return "{} {} Watts is {}.".format(self.__name, self.__watt, self.__status)

all_device = []
while True:
    action = input("(a)dd device, (s)how device, (q)uit\n").lower()
    if action == 'a':
        name = input("Device name : ")
        watt = input("Watt : ")
        status = input("On or Off? : ").title()
        all_device.append(Device(name, watt, status))
    elif action == 's':
        for device in all_device:
            print(device)
    elif action == 'q':
        print("bye")
        break
    else:
        print("Incorrect Input")