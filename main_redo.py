# this is a redo of main.py because there were so many ways i could have improved my code. mainly i didnt pass any variables through
# functions. i feel like im lacking on that aspect.

import os
import random

from art import logo

play = 'y'
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clr():
    os.system('clear')


def deal_card():
    """picks random card from cards list returns int"""
    card = random.choice(cards)
    return card


def calc_score(deck):
    """calculates current score of list of cards and handles ace card functinoallity"""
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)


def compare(p1_score, ai_score):
    """winning logic of game. who wins who loses"""

    if p1_score > 21 and ai_score > 21:
        return "You went over. You lose 😤"
    if p1_score == ai_score:
        return "Draw 🙃"
    elif ai_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif p1_score == 0:
        return "Win with a Blackjack 😎"
    elif p1_score > 21:
        return "You went over. You lose 😭"
    elif ai_score > 21:
        return "Opponent went over. You win 😁"
    elif p1_score > ai_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """contains game logic"""

# initializing game
    clr()
    print(logo)
    global play
    ai_deck = [deal_card(), deal_card()]
    p1_deck = [deal_card(), deal_card()]
    print(f"Dealer Score: {ai_deck[0]} Dealer Hand: {ai_deck[0]}, ?")
    print(f"Your Score: {sum(p1_deck)} Your Hand: {p1_deck}")
    p1_score = calc_score(p1_deck)
    if p1_score == 0:
        hit = 'n'

# does p1 want more cards
    hit = input('Do you want another card? y/n\n').lower()
    while hit == 'y':
        p1_deck.append(deal_card())
        p1_score = calc_score(p1_deck)
        clr()
        print(logo)
        print(f"Dealer Score: {ai_deck[0]} Dealer Hand: {ai_deck[0]}, ?")
        print(f"Your Score: {sum(p1_deck)} Your Hand: {p1_deck}")
        hit = input('Do you want another card? y/n\n')
        if p1_score == 0 or p1_score > 21:
            hit = 'n'

# ai deck logic
    ai_score = calc_score(ai_deck)
    while ai_score != 0 and ai_score < 17:
        ai_deck.append(deal_card())
        ai_score = calc_score(ai_deck)


# win or lose
    clr()
    print(logo)
    print(f"Dealer Score: {ai_score} Dealer Hand: {ai_deck}")
    print(f"Your Score: {sum(p1_deck)} Your Hand: {p1_deck}")
    print(compare(p1_score, ai_score))

# end, play again?
    play = input('\nDo you want to play again? y/n\n')


clr()
play = input('Do you want to play a game of Black Jack? y/n\n').lower()
while play == 'y':
    play_game()
