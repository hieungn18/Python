# Prolog
# Author:  Hieu Nguyen
# Email:  hnguyen182@student.gsu.edu
# Section: Section 004
#Python Lab11 
'''
Purpose:
   Implement the build_dictionary() function to build a word frequency dictionary from a list of words.   
Pre-conditions (input):
    Takes in word as an input. 
Post-conditions (output):
    Displays the dictionary 
'''
def build_dictionary(words):
    dictionary = {}
    
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

def main():
    words = input("\nIf the input is: ").split()
    words_dict = build_dictionary(words)
    for word, freg in sorted (words_dict.items()):
        print(f"\n{word}: {freg}\n")
main()
