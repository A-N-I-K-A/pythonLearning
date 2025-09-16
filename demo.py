# //swap
from sys import argv

# x=5
# y=6
# x,y=y,x
# print(x,y)
# x=x^y
# y=x^y
# x=x^y
# print(x,y)
#
#
# x=int(input("Input a number:"))
# y=int(input("Input a number:"))
# z=x+y
# print(z)
#
# #we only want to input one character
# ch = input("Input a character:")[0]
# print(ch)
#
# #using eval
# result=eval(input("Input an expression:"))
# print(result)

#we can pass values with the python file_name.py val1 val2
#like this, and run it from the terminal
# x=(argv[1])
# y=(argv[2])
# print(x+y)


# i=1
# while i<=5:
#     print(i)
#     i=i+1

#we use pass for empty if,elif or else block
# for i in range(1,10):
#     if i%2==0:
#         pass
#     else:
#         print(i)
#

#for-else
#if there is a break in for loop then if the break is never
#executed it will execute the else statement
# arr=[10,12,14,12,16]
# for i in arr:
#     if i%2!=0:
#         print(i)
#         break
#
# else:
#     print("Not found")

from array import *
# vals=array('u',['a','e','i','o','u'])
# vals1=array('i',[1,2,3,4,5])
# new_vals1=array(vals1.typecode,[e**2 for e in vals1])
# new_vals=array(vals.typecode,[e for e in vals])
# print(new_vals)
# print(new_vals1)
#


#
# from array import *
# arr=array('i',[])
# n=int(input('Enter the length of array:'))
# for i in range(n):
#     x=int(input('Enter the value'))
#     arr.append(x)


from numpy import *
# arr=array([1,2,3,4,5],float)
#
# print(arr.dtype)
# print(arr)


# arr=linspace(0,15,16)
# print(arr)

# arr=arange(1,15,2)
# print(arr)

# arr=logspace(1,40,5)
# print(arr)

# arr=zeros(10,int)
# print(arr)


# arr1=array([1,2,3,4,5])
# arr2=arr1
# print(arr2)
# print(arr1)
# print(id(arr2))
# print(id(arr1))
#
#
# arr1=array([1,2,3,4,5])
# arr2=arr1.view()
# arr1[0]=10
# print(arr2)
# print(arr1)
# print(id(arr2))
# print(id(arr1))
#
# arr1=array([1,2,3,4,5])
# arr2=arr1.copy()
# arr1[0]=10
# print(arr2)
# print(arr1)
# print(id(arr2))
# print(id(arr1))
#

# arr1=array([
#             [1,2,3,4,7,6],
#             [4,5,6,8,9,7]
# ])
#
# print(arr1.ndim)
# print(arr1.shape)
# arr2=arr1.flatten()
# print(arr2)
# arr3=arr2.reshape(2,6)
# print(arr3)
# arr4=arr2.reshape(2,3,2) #gives 2 2d matrix each having 3 1d arrays of 2 items
# print(arr4)

# arr1=array([[1,2,3],[4,5,6],[7,8,9]])
# arr2=matrix(arr1)
# print(arr2)
# arr3=matrix('1 2 3; 4 5 6; 7 8 9')
# print(arr3)
# print(arr3.min())
# print(arr3.diagonal())
# print(arr2*arr3)

# def update(x):
#     print(id(x))#till now the address is same
#     x=8
#     print("x",x)
#     print(id(x))#as we change the value the address will be different
# x=10
# print(id(x))
# update(x)
# print("x",x)
#
#
#
# def update(x):
#     print(id(x))#till now the address is same
#     x[0]=4
#     print("x",x)
#     print(id(x))#the address will be same only
# x=[1,2,3]
# print(id(x))
# update(x)
# print("x",x)


