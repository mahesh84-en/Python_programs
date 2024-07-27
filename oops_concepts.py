#classes are user defined blueprint or prototype

#methods, class variables, constructor

class Calculator:
    num = 100 #class variables
    #default constructor no need to name of the construcor should be class name like java. in python, init should be the name constructor
    def __init__(self,a,b):
        self.a = a
        self.b = b # instance variables
        print("I  will be called automatically when object is created")


    def get_Data(self):
        print("i am executing a method")

    def Summation(self):
        print(Calculator.num)
        return self.a + self.b


obj = Calculator(2,3) #syntax to create object
obj.get_Data()
print(obj.Summation())

#constructor
#a special method called when an object is created when there is no constructor default constructor will be called.
# instance varaibles change according to the object creation but class variables doesn't change
#