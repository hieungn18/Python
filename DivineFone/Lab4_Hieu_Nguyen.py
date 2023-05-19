# Prolog
# Author:  Hieu Nguyen
# Email:  hnguyen182@student.gsu.edu
# Section: Section 004
'''
  Purpose:
    Phone number breakdown
  Pre-conditions (input):
    (Enter the 10-digit phone number)
  Post-conditions (output):
    Breakdown of phone number (area code, prefix, line number)
'''
def main():
# Design and implementation
#  1.  Output a message to identify the program, and a blank line
    print("Breakdown of phone number to area code, prefix, line number ")
    print()
#  2.  Input the 10-digit phone number
    phone_number = (input ("Enter your phone number: "))
#  3.  Breakdown the phone number
    area_code = str(phone_number[0:3])
    prefix = str(phone_number[3:6])
    line_number = str(phone_number[6:10])
#  4. Output breakdown to area code, prefix, line number
    print()
    print("Phone number is   (%s)%s-%s " % (area_code,prefix, line_number))
    print()
    print("Phone number is converted  to area = (%s), prefix = %s, line number = %s " % (area_code, prefix, line_number))
main()
# end of program file

'''
    Find the syntax error and document itand fix it

Line 23, it had syntax error: it was invalid character ( '‘' (U+2018))
It did not have close ")"
After line 13, it was IndentationError: expected an indented block after function definition on line 13
    Find the semantics error and documentit and fix it

It was missing the code for break down the phone number.
It had extra the phone_str variable unnecessary. 
I put in the code with str() and count the posistion of the phone number. 
'''
