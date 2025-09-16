class A:
    def __init__(self):
        print("A init")
    def feature1(self):
        print("Feature 1-a working")
    def feature2(self):
        print("Feature 2 working")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")
    def feature1(self):
        print("Feature 1-b working")
    def feature2(self):
        print("Feature 2 working")

class C(A,B):
    def __init__(self):
        print("C init")
        super().__init__()
        super().feature1()

a1=C()
a1.__init__()
a1.feature1()
