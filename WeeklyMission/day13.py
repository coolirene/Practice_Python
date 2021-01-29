# Day 13. Class and Constructor - Create Calculator with Class and Constructor
# class
class Calculator:
    # create constructor using _init_() - parameterize
    def __init__(self, x, y):
        self.x = x
        self.y =y
    #  
    def add(self):
        result =  self.x + self.y
        return result
    
    def subt(self):
        result =  self.x - self.y
        return result

    def mul(self):
        result = self.x * self.y
        return result
    
    def div(self):
        result =  self.x / self.y
        return result

fnum = float(input("Enter First Number : "))
snum = float(input("Enter Second Number : "))
# Create cal object of Calculator class - invoke the constructor
cal = Calculator(fnum, snum)
# perform methods
print(cal.add())
print(cal.subt())
print(cal.mul())
print(cal.div())