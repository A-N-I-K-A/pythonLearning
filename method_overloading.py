class Student:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def sum(self,a=None,b=None,c=None):
        n=0
        if a!=None and b!=None and c!=None:
            n=a+b+c
        elif a!=None and b!=None:
            n=a+b
        else:
            n=a
        return n

s1=Student(78,89)
print(s1.sum(3,4))