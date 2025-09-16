class Computer:
    wheels=4 #class variable/static variables
    def __init__(self,cpu,ram):
        #special method
        self.cpu=cpu #instance variable
        self.ram=ram


    def config(self):
        print(self.cpu," ",self.ram)

    def compare(self,other):
        if self.cpu==other.cpu:
            return True
        else:
            return False


comp1=Computer("i5",16)
comp2=Computer("i5",8)
comp1.config()
comp2.config()
print(id(comp1))
print(id(comp2))
print(comp1.compare(comp2))

print(comp1.cpu,comp1.ram,comp1.wheels)
print(comp2.cpu,comp2.ram,comp2.wheels)
