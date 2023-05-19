# Prolog
# Author:  Hieu Nguyen
# Email:  hnguyen182@student.gsu.edu
# Section: Section 004
#Python Lab9 activity 1
'''
Purpose:
    Use function to calculate the number of miles.  
Pre-conditions (input):
    Take number of laps as an input.
Post-conditions (output):
    Print out the output the numbers of mile
'''
# This is function use to calculate the lap to miles.
def laps_to_miles(user_laps):
    user_miles =  user_laps * 0.25
    return user_miles
# This is the main function take inputs from user to calculate to miles.
def main():
    user_laps = float(input("\nIf the input is: "))
    a = laps_to_miles(user_laps)
    print(f"\nThe out put: {a:.2f}\n")
main()