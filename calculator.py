# %% Calculator
class Calculate(object):
    def __init__(self,a,b):
        self.v1 = a
        self.v2 = b
    def add(self):
        #adding
            return (self.v1 + self.v2)
    def multiply(self):
        #multiplication
                return (self.v1 * self.v2)
            #choosing process
process = input("Select a process 1 for adding 2 for multipication")
#getting value_1
v2 = int(input("First Value"))
#getting value_2
v1 = int(input("Second Value"))
c1 = Calculate(v1, v2)
#printing result with a simple condition
if (process == "1"):
    print(c1.add())
elif(process == "2"):
    print(c1.multiply())

