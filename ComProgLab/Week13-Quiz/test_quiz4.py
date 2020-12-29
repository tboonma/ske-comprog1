class Device:
    def __init__(self, name="None", watt=0, status="Off"):
        self.__name = name
        self.__watt = watt
        self.__status = status
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def watt(self):
        return self.__watt
    
    @watt.setter
    def watt(self, value):
        self.__watt = value
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        self.__status = value
    
    def __str__(self):
        return "{} {} Watts is {}.".format(self.__name, self.__watt, self.__status)

all_device = []
while True:
    action = input("(a)dd device, (s)how device, (q)uit\n").lower()
    if action == 'a':
        all_device.append(Device())
        pos = len(all_device)-1
        all_device[pos].name = input("Device name : ")
        all_device[pos].watt = input("Watt : ")
        all_device[pos].status = input("On or Off? : ").title()
    elif action == 's':
        for device in all_device:
            print(device)
    elif action == 'q':
        print("bye")
        break
    else:
        print("Incorrect Input")