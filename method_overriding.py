class A:
    def show(self):
        print("in A show")

class B(A):
    #if we do not have a show method in B
    #then it will print the show form A

    #if we do have a show method in B
    #then it will print the show in B
    def show(self):
        print("in B show")

a1=B()
a1.show()