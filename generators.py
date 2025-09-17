# def topten():
#     yield 5
#
#
# values=topten()
# #will return a generator object
# print(values)
# #will return the value
# print(values.__next__())

def topten():
    n=1

    while n<=10:
        sq=n*n
        yield sq
        n+=1

values=topten()
for i in values:
    print(i)