"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    #  initialize the constants
    stones = 20  # initializes the number of stones for 20
    player = 1  # initializes the player as player 1 and line 20 interchanges
# first step: ask the user to pick 1 or 2 stones.
    while stones > 0:  # runs for as long as stones are more than 0
        remove = int(input("player " + str(player) + " Would you like to remove 1 or 2 stones?"))
        while remove < 1 or remove > 2:
            print("Error: Enter 1 or 2 ")
            remove = int(input("player " + str(player) + " Would you like to remove 1 or 2 stones?"))
        # this asks the user to remove any number of stones
        stones -= remove  # this subtracts the number entered by the user from the original amount of stones available
        print("There are " + str(stones) + " left")  # returns the number of stones of stones left after being deducted
        player = 3 - player  # this will either return player as player 1 or player 2 so it is good to use such when
        # you want to go back and forth with numbers in a loop
    if player == 1:
        player = 1
    else:
        player = 2
    print("player " + str(player) + " wins!")
    print("Game over")  # ends the loop when stones are finished

"""
def main():
    #  initialize the constants
    stones = 20  # initializes the number of stones for 20
    player = 1  
    print("There are " + str(stones) + " stones left") # initializes the player as player 1 and line 20 interchanges
# first step: ask the user to pick 1 or 2 stones.
    while stones > 0:
        # runs for as long as stones are more than 0
        remove = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
        while remove < 1 or remove > 2:
            remove = int(input("Please enter 1 or 2: "))
        # this asks the user to remove any number of stones
        stones -= remove
        print("")
        # this subtracts the number entered by the user from the original amount of stones available
        if stones != 0: # stops the code from returning 0 stones left
            print("There are " + str(stones) + " stones left")  # returns the number of stones of stones left after being deducted
        player = 3 - player  # this will either return player as player 1 or player 2 so it is good to use such when
        # you want to go back and forth with numbers in a loop
    if player == 1:
        player = 1
    else:
        player = 2
    print("Player " + str(player) + " wins!")
     # ends the loop when stones are finished
    """

if __name__ == '__main__':
    main()

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
