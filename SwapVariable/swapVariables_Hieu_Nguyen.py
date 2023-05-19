# Prolog
# Author:  Hieu Nguyen
# Email:  hnguyen182@student.gsu.edu
# Section: Section 004
#Python Lab10 activity 2
'''
Purpose:
    Use the function to swap the position of the value 
Pre-conditions (input):
    Take integer as an input.
Post-conditions (output):
    Print out the swap value on single line.
'''
def swap_value(val1,val2,val3,val4):
    a = val1
    val1 = val2
    val2 = a

    b = val3
    val3 = val4
    val4 = b

    return val1, val2, val3, val4
def main():
    num1 = int(input("The 1st value: "))
    num2 = int(input("The 2nd value: "))
    num3 = int(input("The 3rd value: "))
    num4 = int(input("The 4th value: "))

    num1, num2, num3, num4 = swap_value(num1,num2, num3, num4)
    print( num1," ", num2," ", num3," ", num4,"",)
main()