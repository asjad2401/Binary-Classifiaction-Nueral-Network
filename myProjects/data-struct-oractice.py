"""string = input("Enter a string: ")
ans = ""
for x in string:
    if x not in "aeiouAEIOU":
        ans += x
    else:
        ans += " "
print(ans) 
=============================================================
year = int(input("Enter a year: "))

if (year%400) == 0 or ((year%4) ==0 and not (year%100) ==0):

      print("leap")

else:

      print("not a leap") 
=============================================
l = [50,40,25,41,29]
price =0
for p in l:
    price = price + p
print(price) 
=================================


for n in range(2, 21, 2) :
    print(n)

    =======================================
n = int(input("Enter a number: "))

sum = 0
x =0
while x <= n:

      sum = sum + x

      x = x+1

print(sum)
==================================


list = [3,5,9,3,2,9,10]

for x in list:
      print(x)

======================================

tuple = ("one","two"," three","four","five")

for x in tuple: 

      print(len(x))
============================================
x = 0
 
while (x < 100):
    x = x + 2
 
print(x)
==========================================
def calculation(a,b,sig):

      if sig == "+" :

            return(a+b)

      else:

        return(a-b)

x,y,sign = int(input("Number1: ")) , int(input("Number2: ")) , input("operator + or - : ")

result = calculation(x,y,sign)

print(result)
==========================================

def showEmployee(name,salary):

      print("Employee "+ name + " salary is " + str(salary))

showEmployee("sam", 9000)
============================================


def outer(a,b):

    def inner(c,d):

         return c+d

    return 8 + inner(a,b)

print (outer(5,10))
==============================================
"""

import numpy as np

# Given matrix A
A = np.array([[2, 4, 5], [8, 2, 4], [5, 8, 2]])

# Given inverse matrix A_inv from your program output
A_inv = np.array([[-0.14, 0.16, 0.03],
                  [-0.02, 0.106, -0.16],
                  [0.27, 0.02, -0.14]])

# Verify if AA_inv is approximately the identity matrix
result = np.dot(A, A_inv)
identity_matrix = np.identity(3)

print("Result of multiplication:")
print(result)
print("\nIdentity matrix:")
print(identity_matrix)
