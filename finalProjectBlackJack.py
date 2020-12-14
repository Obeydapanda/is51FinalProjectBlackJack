"""""
import random

deck [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
#using deck as a global variable

def deal(deck):
    hand = []
    for i in range (2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11: card = "Jack"
        if card == 12: card = "Queen"
        if card == 13: card = "King"
        if card == 14: card = "Ace"
        hand.append(card)
    return hand
#deals out the user/dealers hand

def hit(hand):
    card = deck.pop()
    if card == 11:
         card = "Jack"
    if card == 12: 
        card = "Queen"
    if card == 13: 
        card = "King"
    if card == 14: 
        card = "Ace"
    hand.append(card)
    return(hand)
#adds a new card to either dealer if < 17 and the user when wanted to, and changes jack, queen, king, and ace to their values with ace changing afterwards

def total(hand):
    total = 0
    for card in hand:
        if card == "Jack" or card == "Queen" or card == "King":
            total += 10
        elif card == "Ace":
                if total >= 11: total += 1
                else: total+= 11
        else: total += card
    return total
#sums up user and dealer's hands when showing results before and after being hit

def blackjack(dealer_hand, user_hand):
    if user_hand == 21:
        print(Congrats! you won by hitting blackjack)
        restart
    elif dealer_hand == 21:
        print (sorry, you lost with dealer hitting blackjack)
#checks to see if you or the dealer hit blackjack initially

def again():
    choice input("Play again? (Yes/No)").lower
    if yes:
        dealer_hand = []
        user_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        main()
    else
        goodbye
        exit
#restarts the game and resets the values for deck, user and dealer


def evaluate(dealer_hand, user_hand):
    if total(user_hand) == 21:
        print("Congrats! You have gotten BlackJack! with ", user_hand)
        #if the user gets 21
    elif total(dealer_hand) == 21:
        print("Sorry, Dealer has gotten BlackJack with ", dealer_hand)
        #if the dealer gets to 21
    elif total(dealer_hand) == total(user_hand):
        print ("Both you and the dealer had the same amount of points \n", "User at \n", total((user_hand)), "Dealer at ", total((dealer_hand)))
        #if you and the dealer have the same hand
    elif total(user_hand) > 21:
        print("Sorry, your hand was ", total((user_hand)), " going over your 21 which means you lost")
        #if the user goes over 21
    elif total(dealer_hand) > 21:
        print ("Congrats! Dealer had", total((dealer_hand)), " and went over 21 and you win!")
        #if the dealer goes over 21
    elif total(user_hand) > total(dealer_hand):
        print("Congrats! You Win, your ", total((user_hand)), " was higher than the dealers ", total((dealer_hand)))
        #if the user has a higher number than the dealer but both are under 21
    elif total(dealer_hand) > total(user_hand):
        print("Sorry, You lost, your ", total((user_hand)), " was lower than the dealers ", total((dealer_hand)))
        #if the dealer is higher than the user, but both are still under 21
#evaluates on who won based on the conditions

def main():
    choice = 0
    dealer_hand = deal(deck)
    user_hand = deal(deck)
    print("Welcome to BlackJack!\n")
    while choice != "Quit":    
        print("The Dealer is showing a ", dealer_hand[0])
        print("Your hand consist of ", str(user_hand), " for a total of ", str(total(user_hand)))
        blackjack(user_hand, dealer_hand)
        choice = input("Do you want to [Hit], [Stay] or [Quit]?\n").lower()
        if choice == "hit":
            hit(user_hand)
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            evaluate(dealer_hand, user_hand)
            again()
        elif choice == "stay":
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            evaluate(dealer_hand, user_hand)
            again()
        elif choice == "quit":
            print("Good Bye! Hope you liked it")
            exit()
#where everything happens

main()



"""