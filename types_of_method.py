class Student:
    school="Telusko"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        #accessor methods
        return self.m1

    def set_m1(self,value):
        #mutator methods
        self.m1=value

    @classmethod
    #to use a class method we have to use decorators
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print("Everything is working---")


s1=Student(12,34,56)
s2=Student(56,23,45)

print(s1.avg())
print(s2.avg())

s1.set_m1(20)
print(s1.get_m1())

print(Student.get_school())

Student.info()

