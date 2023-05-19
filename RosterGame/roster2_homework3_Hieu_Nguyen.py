# Prolog
# Author:  Hieu Nguyen
# Email:  hnguyen182@student.gsu.edu
# Section: Section 004
# Python: Homework 3 
'''
Purpose:
    We are going to build a roster managementfor the Atlanta Braves(World series Champions). However, each players have some stats that we are going to store.
Pre-conditions (input):
    Take in the name and the stats of batter only. 
Post-conditions (output):
    Print out the roster that contain the name and the stats of the player.
'''
"""
#main function
create a method that will look up a player and return the name of that player in the roster.
create a method that will add a player include name and his stats into a roster, and it will count on if they have same name.
create a method that will delete the name of player in the roster that include his stats.
create a method that will display the roster after modification.
create a main function 
  #display introductory message
create a print out introductory message
create a roster that will cointain all the name and stats of players.
ask for the choice from the user.
If user choose to look up for the player:
  it will get the name of the player and print out the stats if it is already in the roster. If it is no in the roster, the message will print out that lets the user know that player is not in the roster.
If user choose to add the player to the roster:
  it will ask user the name and the stat of the player then it will bring out all the players in the roster.
If user choose to remove the player in the roster:
  it will ask the name of the player in the roster. If that player is not in the roster , another message will print out that lets user know that player is not in the roster or the user missed type.
Last condition will be choose to exit the program or the user has to choose valid option again.
"""
import unittest
# method to search for a player in the roster
def lookup_player(brave_roster, name):   
    return brave_roster.get(name,"N/A")

# method to add a player to the roster
def add_player_to_dict(brave_roster, name, stats):
    if name in brave_roster:
        # If so, modify the player name to add a suffix
        suffix = 2
        while f"{name}({suffix})" in brave_roster:
            suffix += 1
        name = f"{name}({suffix})"
    brave_roster[name] = stats
    return brave_roster
# method to remove a player
def delete_in_dict(brave_roster, name):
    removePlayer = brave_roster.pop(name, "")
    if removePlayer == "":
        print("uh typo? " + name + " does not play for us :)")
    else:
        display_roster(brave_roster)
    return brave_roster
#display the player from the roster
def display_roster(brave_roster):
    print("\nHere's the complete team roster:")
    for n, s in brave_roster.items():       
        print("\t" + n + ":" + s)
    print("\nThanks for using My Braves Stats.")      
    return brave_roster

def main():
# initial roster
  brave_roster = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273",
		"Ronald Acuna": "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266",
  }
# your code here 
  # display a welcome message and menu
  while True:
        print("\n\t*** Braves Stats ***")
        print("Welcome to My Braves Stats! What can I do for you?\n")
        print("\t1. Search for a player"
              "\n\t2. Add a new player"
              "\n\t3. Remove a player"
              "\n\t0. Exit and run the Test case")
        #get input from user
        user_input = int(input("\nPlease type your choice number: "))
        #user chooses to search for a player
        if user_input == 1:
            name = input("\nEnter the name of the player you want to look up: ")
            stats = lookup_player(brave_roster, name)
            if stats == "" or stats =="N/A":
                print("\nuh typo? " + name + " does not play for us:)")
            else:
                print("\nHere's are " + name + " stats: " + stats)
                print("\nThanks for using My Braves Stats.")
        #user chooses to add for a player
        elif user_input == 2:
            name = input("\nEnter the name of the player you want to add: ")
            stats = input("\nPlease add " + name + "'s stats: ")
            brave_roster = add_player_to_dict( brave_roster, name, stats)
            display_roster(brave_roster)
        #user chooses to remove for a player
        elif user_input == 3:
            name = input("\nEnter the name of the player you want to remove: ")
            brave_roster = delete_in_dict(brave_roster, name)
        elif user_input < 0 or user_input > 3:
            print("\nInvalid choice!\n"
                  "\nPlease choose again! From 1 to 3\n")
        else:
            break
main()

# Testing code
class TestDictFunctions(unittest.TestCase):

  def test_search_player_success(self):
    test_dict = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"
    }
    actual = test_dict["Austin Riley"]
    expected = lookup_player(test_dict, "Austin Riley")
    self.assertEqual(actual, expected)

  def test_search_player_no_result(self):
    test_dict = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"
    }
    actual = "N/A"
    expected = lookup_player(test_dict, "Ronald Acuna")
    self.assertEqual(actual, expected)

  def test_add_player_sucess(self):
    test_dict = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"
    }
    actual = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273",
		"Ronald Acuna": "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266"
    }
    expected = add_player_to_dict(test_dict, "Ronald Acuna", "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266")

    self.assertEqual(actual, expected)

  def test_add_player_duplicate(self):
    test_dict = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"}
    actual = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273", "Austin Riley(2)": "AB: 350, R: 20, H: 120, HR: 5, AVG: 0.214"}
    expected = add_player_to_dict(test_dict, "Austin Riley", "AB: 350, R: 20, H: 120, HR: 5, AVG: 0.214")
    self.assertEqual(actual, expected)

  def test_delete_player_sucess(self):
    test_dict = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"}
    expected = {}
    actual = delete_in_dict(test_dict, "Austin Riley")
    self.assertEqual(actual, expected)

  def test_delete_word_no_result(self):
    test_dict = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"}
    expected = test_dict
    actual = delete_in_dict(test_dict, "Shohei Ohtani")
    self.assertEqual(actual, expected)


#uncomment to run tests
unittest.main()

