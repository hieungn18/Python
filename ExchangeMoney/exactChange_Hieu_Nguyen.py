# Prolog
# Author:  Hieu Nguyen
# Email:  hnguyen182@student.gsu.edu
# Section: Section 004
#Python Lab10 activity 1
'''
Purpose:
    Use the function to calculate exact change amount of fewest coin.  
Pre-conditions (input):
    Take integer as an input.
Post-conditions (output):
    Print out the change, one typer per line.
'''

def exact_change(user_total):
    quarter = user_total // 25
    user_total %= 25

    dime = user_total // 10
    user_total %= 10

    nickel = user_total // 5
    user_total %= 5

    penny = user_total 
    
    return penny, nickel, dime, quarter

def main():
    input_val = int(input("Enter the number here: "))
    penny, nickel, dime, quarter = exact_change(input_val)

    if(input_val <= 0):
        print('No Change')
    else:
        if quarter >= 1:
            if quarter == 1 :           
                print(str(quarter)+ " quarter")
            else:
                print(str(quarter)+ " quarters")
        
        if dime >= 1:
            if dime ==1:
                print(str(dime)+ " dime")
            else:
                print(str(dime)+ " dimes")   

        if nickel >= 1:
            if nickel == 1:
                print(str(nickel)+ " nickel")
            else:
                print(str(nickel)+ " nickels")
        if penny >= 1:
            if penny == 1:
                print(str(penny)+ " penny")
            else:
                print(str(penny)+ " pennies")
main()     

        

        

        