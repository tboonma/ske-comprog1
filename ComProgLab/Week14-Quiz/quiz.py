import time

def current_time():
    return time.time()

class Route:
    def __init__(self, name):
        self.__name = name
        self.__bus = []
    
    @property
    def name(self):
        return self.__name
    @property
    def bus(self):
        return self.__bus

    def __str__(self):
        return self.__name
    
class Bus:
    def __init__(self, name):
        self.__name = name
        self.__start = 0
        self.__current_time = 0
        self.__all_time = 0
        self.__status = 'Stop'
    
    @property
    def name(self):
        return self.__name
    
    @property
    def current_time(self):
        if self.__status == 'Running':
            elapse = current_time() - self.__start
            return f"{elapse:.0f}"
        return f"{self.__current_time:.0f}"
    
    @property
    def all_time(self):
        return f"{self.__all_time:.0f}"
    
    @property
    def status(self):
        return self.__status
    
    def run_bus(self):
        self.__start = current_time()
        self.__status = 'Running'

    def stop_bus(self):
        self.__all_time += current_time() - self.__start
        self.__current_time = 0
        self.__status = 'Stop'
    
class Application:
    def __init__(self):
        self.__routes = []
    
    def new_route(self):
        name = input("Enter route name : ")
        self.__routes.append(Route(name))
        self.show_route()

    def choose_route(self):
        route_number = int(input("Enter a route number: ")) - 1
        while True:
            bus = self.__routes[route_number].bus
            action = input("(a)dd bus, (p)rint, (r)un/stop, (m)ain menu: ").lower()
            if action == 'a':
                bus_code = input("Bus Code : ")
                bus.append(Bus(bus_code))
            elif action == 'p':
                print(f'Route {route_number + 1} : {self.__routes[route_number]}')
                self.show_bus(bus)
            elif action == 'r':
                number = int(input("Bus Number? : ")) - 1
                if bus[number].status == 'Stop':
                    bus[number].run_bus()
                else:
                    bus[number].stop_bus()
                print(f'Route {route_number + 1} : {self.__routes[route_number]}')
                self.show_bus(bus)
            elif action == 'm':
                break
            else:
                print("Incorrect Menu")
    
    def show_route(self):
        for i, route in enumerate(self.__routes, 1):
            print(f'Route {i} : {route}')
    
    def show_bus(self, bus):
        for i, b in enumerate(bus, 1):
            print(f"{i}.{b.name} is {b.status} (Current {b.current_time} secs / All {b.all_time} secs)")


app = Application()
while True:
    action = input('(n)ew Route, (s)how, (c)hoose, (q)uit : ').lower()
    if action == 'n':
        app.new_route()
    elif action == 's':
        app.show_route()
    elif action == 'c':
        app.choose_route()
    elif action == 'q':
        print("Bye")
        break
    else:
        print("Incorrect Menu")