class AllPlayer:
    def __init__(self, name, gender, region, budget, numwins, numlosses):
        self.__name = name
        self.__gender = gender
        self.__region = region
        self.budget = int(budget)
        self.__numwins = int(numwins)
        self.__numlosses = int(numlosses)
    
    @property
    def name(self):
        return self.__name
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def region(self):
        return self.__region
    
    @property
    def numwins(self):
        return self.__numwins
    
    @property
    def numlosses(self):
        return self.__numlosses
    
    def add_one_win(self):
        self.__numwins += 1
    
    def add_one_lose(self):
        self.__numlosses += 1