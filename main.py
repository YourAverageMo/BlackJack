import os
import random

from art import logo

############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ai_score = 0


def clr():
    os.system('clear')


clr()
print(logo)


def ai():
    ai_cards = []
    global ai_score
    ai_score = 0
    while ai_score < 17:
        # currently this function only decides if the ace should be 11 or 1 as its being added to the house's deck not after its been placed
        # so for instance if the current deck is 11, 2 and the next card is an ace its not ganna go back and change the 11 to a 1.
        # the reason for this is that the logic for when is the best time to use an 11 vs a 1 gets way to complex for the scope of this project
        # so im leaving it like this maybe the teacher knows a simplier way of implementing that decision making. we shall see....
        new_card = random.choice(cards)
        if new_card == 11 and sum(ai_cards) < 10:
            new_card = 11
        if new_card == 11 and sum(ai_cards) > 10:
            new_card = 1
        ai_cards.append(new_card)
        ai_score += new_card
    return ai_cards


def gamelogic():
    ai_cards = ai()
    p1_cards = []
    p1_cards.append(random.choice(cards))
    p1_score = sum(p1_cards)
    hit = ''
    print((f"The house has a {ai_cards[0]}.\n"))
    hit = input(
        (f"Your cards are {p1_cards}.Your score is {p1_score}.\nDo you want another card? y/n?\n")).lower()
    clr()

    while hit == 'y':
        p1_cards.append(random.choice(cards))
        p1_score = sum(p1_cards)
        print((f"The house has {ai_cards[0]}.\n"))
        hit = input(
            (f"Your cards are {*p1_cards,}.Your score is {p1_score}.\nDo you want another card? y/n?\n")).lower()
        clr()

    if p1_score > 21:
        result = "Sorry you lose."
    elif ai_score > 21:
        result = "You win!"
    elif p1_score == ai_score:
        result = "The game ends in a draw."
    elif p1_score > ai_score:
        result = "You win!"
    else:
        result = "Sorry you lose."

    return (
        f"The house had {*ai_cards,} with a score of {ai_score}.\n{result}\nYour final score was {p1_score}\n"
    )


def another_game():
    more = input("Do you want to play BlackJack? y/n?\n").lower()
    clr()
    while more == 'y':
        # dont put game logic here. put game logic in game_logic func
        print(gamelogic())
        more = input("Do you want to play another game y/n?\n").lower()
        clr()


another_game()
