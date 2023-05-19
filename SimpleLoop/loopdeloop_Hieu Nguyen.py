# Prolog
# Author:  Hieu Nguyen
# Email:  hnguyen182@student.gsu.edu
# Section: Section 004
#Python Lab8
'''
Purpose:
    Using loops to execute the functions.
Pre-conditions (input):
    Making a def for each step.
Post-conditions (output):
    Print out the output. 
'''
#1 Make a list
def makelist(n):
    a= []
    for i in range(n):
        a.append(i)
    return a
print(makelist(10))
print(makelist(3))
print()

#2 Lift off!
def rocketcountdown(n):
    a = []
    for i in range(n,0,-1):
        a.append(i)
    a.append("We lift off!")
    return a
print(rocketcountdown(10))
print(rocketcountdown(2))
print()

#3 Double loop
def doubleloop(n,m):
    a = []
    for i in range(n):
        for j in range(m):
            a.append("{},{}".format(i,j))
    return a
print(doubleloop(2,2))
print(doubleloop(3,4))