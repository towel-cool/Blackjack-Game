# Diego Diaz
# CPS109 Assignment 1

# Note: There are no aces, and if you get the same number as the dealer you win
import random

# A function to play a hand of blackjack, which returns 'win' or 'lose' depending on if the player wins or loses
def hand():
    # Gives the dealer and player their first cards. (Dealer is given 1 random number (1 Card) and the player is given 2 Random numbers (2 Cards) 
    dealer_hand = random.randrange(2,11)
    player_hand = random.randrange(2,11) + random.randrange(2,11)
    # All numbers added are between 2 and 10 (inclusive) because each card in a deck (besides ace) is worth 2 to 10 

    win = False
    lose = False

    # Continues the loop as long as the player has not won or lost
    while win != True and lose != True:
        print("\n**********************\nDealer's Hand:", dealer_hand)
        print("Your Hand:", player_hand, "\n**********************")

        # Asks if the player would like to hit or stand, and saves their input
        hit_or_stand = input("Hit or Stand? (H/S)\n")
    
        # Checks if the player wants to hit or stand
        if hit_or_stand == "H":
            # If the player decides to hit, another random number (card) is added to their total number (hand)
            player_hand += random.randrange(2,11)
        elif hit_or_stand == "S":    
            # If the player decides to stand, the dealer draws more cards until they have more than 16 cards (as per blackjack rules)
            while (dealer_hand <= 16):
                dealer_hand += random.randrange(2,11)
            # If the dealer doesnt go over 21, and has a higher number than the player, the player loses
            if (dealer_hand <= 21 and dealer_hand > player_hand):
                lose = True
                print("**********************\nDealer's Hand:", dealer_hand, "\nYour Hand:", player_hand, "\nYou Lost this hand" )
                return "lose"
                break
            # If the dealer has less than 21 and the player has a higher number, the player wins
            elif (dealer_hand <= 21 and player_hand > dealer_hand):
                win = True
                print("**********************\nDealer's Hand:", dealer_hand, "\nYour Hand:", player_hand, "\nYou Won this hand" )
                return "win"
                break
            # If the dealer goes over 21, the players wins
            else:
                win = True
                print("**********************\nDealer's Hand:", dealer_hand, "\nYour Hand:", player_hand, "\nYou Won this hand" )
                return "win"
                break
        # If the player goes over 21 they lose
        if (player_hand > 21):
                lose = True
                print("**********************\nDealer's Hand:", dealer_hand, "\nYour Hand:", player_hand, "\nYou Lost this hand" )
                return "lose"
        # If the dealer goes over 21, the player wins
        elif (dealer_hand > 21):
            win = True
            print("**********************\nDealer's Hand:", dealer_hand, "\nYour Hand:", player_hand, "\nYou Won this hand" )
            return "win"

# Sets a default amount of points for the player to start with
points = 100

print("Reach 500 points to win!")

#Continues to loop as long as the player hasnt won or lost
while points > 0 and points < 500: 
    valid_wager = False

    print("\nPoints:", points)
    wager = int(input("How many points would you like to wager?\n"))

    # Makes sure the player cant wager more points than they have
    while valid_wager == False:
        # If the player tries to wagers more than they have, they are told they dont have that many points and are prompted to enter another number
        if wager > points:
            print("You only have", points, "Points...")
            wager = int(input("How many points would you like to wager?\n"))
        #If the player enters a value that is valid (they have as many points has they wagered), the loop is broken and they can play another hand
        else:
            valid_wager = True
    # Calls the hand function, which makes the player play a hand, and returns whether they won or lost.
    result = hand()
    # Depending on the result of the hand, the player either doubles what they wagered, or loses their wager
    if result == "win":
        points = points + wager
    else: 
        points = points - wager

# Checks whether the player achieved 500 points, or if they reached 0 and prints a statement accordingly
if points >= 500:
    print("\nYou reached 500 points! \nYou Win! :D")
else: print("\nYou ran out of points\nYou Lose :(")