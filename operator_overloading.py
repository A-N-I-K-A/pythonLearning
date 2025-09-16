class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3

    def __gt__(self, other):
        m1=self.m1+self.m2
        m2=other.m1+other.m2
        if m1>m2:
            return True
        else:
            return False

    def __str__(self):
        #return a string
        #just writing return self.m1,self.m2 will return a tuple
        return "{} {}".format(self.m1,self.m2)

s1=Student(56,78)
s2=Student(60,78)


s3=s1+s2
print(s3.m1)

if s1>s2:
    print("Good job s1")
else:
    print("Good job s2")

print(s1.__str__()) #if we dont override the __str__ function then print(s1.__str__()) it will print the address
#now print(s1) will also work
print(s1)