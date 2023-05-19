# Prolog
# Author:  Hieu Nguyen
# Email:  hnguyen182@student.gsu.edu
# Section: Section 004
#Python Lab11 
'''
Purpose:
    A contact list is a place where you can store a specific contact with other associated information such as a phone number, email address, birthday, etc.  
Pre-conditions (input):
    Takes in word pairs that consist of a name and a phone number (both strings). 
Post-conditions (output):
    The phone number associated with that name.
'''


def main():
    
    user_input = input("\nInput name and contact number: ").upper().split()
    contacts = {} 
      
    for i in range (0, len(user_input),2):
        contacts[user_input[i]] = user_input[i+1]
        
    name = input("\nFind your contact name: ").upper()
    phone = contacts[name]
    print("\nPhone number is: ",phone,'\n')
    
    
main()