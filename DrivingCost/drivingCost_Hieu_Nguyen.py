# Prolog
# Author:  Hieu Nguyen
# Email:  hnguyen182@student.gsu.edu
# Section: Section 004
#Python Lab9 activity 2
'''
Purpose:
    Use function to calculate gas cost.  
Pre-conditions (input):
    Take number of miles as an input.
Post-conditions (output):
    Print out the output the numbers of miles
'''
# This function call to calculate the mile driven.
def driving_cost(mile_per_gallon, dollar_per_gallon, mile_driven):
    
    driven = (mile_driven/mile_per_gallon) * dollar_per_gallon
    return driven
# This is the main function that take input from user as mile per gallon, cost per gallon, and mile driven.
def main():
    mile_per_gallon = float(input("\nHow many miles per gallon: "))
    dollar_per_gallon = float(input("\nHow much per gallon: "))
    
    a = driving_cost(mile_per_gallon, dollar_per_gallon,10)
    b = driving_cost(mile_per_gallon, dollar_per_gallon,50)
    c = driving_cost(mile_per_gallon, dollar_per_gallon,400)

    print(f"\nThe out put for 10 miles is: {a:.2f}\n")
    print(f"The out put for 50 miles is: {b:.2f}\n")
    print(f"The out put for 400 miles is: {c:.2f}\n")

main()