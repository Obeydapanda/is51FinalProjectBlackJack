
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4


def deal(deck):
    hand = []
    for i in range (2):
        random.shuffle(deck)
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
    return hand

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


def total(hand):
    total = 0
    for card in hand:
        if card == "Jack" or card == "Queen" or card == "King":
            total += 10
        elif card == "Ace":
                if total >= 11: 
                    total += 1
                else: total+= 11
        else: total += card
    return total

        
def again():
    choice = input("Would you like to play again? (Yes/No)\n").lower()
    if choice == "yes":
        dealer_hand = []
        user_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        main()

    else:
        print("Good Bye!")
        exit()

def blackjack(user_hand, dealer_hand):
    if total(user_hand) == 21:
        print("Congratualtions! you got Blackjack with ", user_hand, "\n")
        again()
    elif total(dealer_hand) == 21:
        print("Sorry, Dealer has gotten BlackJack with ", dealer_hand, "\n")
        again()

def evaluate(dealer_hand, user_hand):
    if total(user_hand) == 21:
        print("Congrats! You have gotten BlackJack! with ", user_hand)
        #if the user gets 21
    elif total(dealer_hand) == 21:
        print("Sorry, Dealer has gotten BlackJack with ", dealer_hand)
        #if the dealer gets to 21
    elif total(dealer_hand) == total(user_hand):
        print ("Both you and the dealer had the same amount of points \n", "User at", total((user_hand)), "\n Dealer at ", total((dealer_hand)))
        #if you and the dealer have the same hand
    elif total(user_hand) > 21:
        print("Sorry, your hand was ", total((user_hand)), " going over your 21 which means you lost")
        #if the user goes over 21
    elif total(dealer_hand) > 21:
        print ("Congrats! Dealer had", total((dealer_hand)), " and went over 21 and you win! You had ", total((user_hand)))
        #if the dealer goes over 21
    elif total(user_hand) > total(dealer_hand):
        print("Congrats! You Win, your ", total((user_hand)), " was higher than the dealers ", total((dealer_hand)))
        #if the user has a higher number than the dealer but both are under 21
    elif total(dealer_hand) > total(user_hand):
        print("Sorry, You lost, your ", total((user_hand)), " was lower than the dealers ", total((dealer_hand)))
        #if the dealer is higher than the user, but both are still under 21
    

def main():
    choice = 0
    #repeat = 0
    dealer_hand = deal(deck)
    user_hand = deal(deck)
    print("\n Welcome to BlackJack!\n")
    while choice != "Quit":    
        print("The Dealer is showing a ", dealer_hand[0] , "and an unknown")
        print("Your hand consists of ", str(user_hand), " for a total of ", str(total(user_hand)))
        blackjack(user_hand, dealer_hand)
        choice = input("Do you want to [Hit], [Stay] or [Quit]?\n").lower()
        if choice == "hit":
            hit(user_hand)
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            evaluate(dealer_hand, user_hand)
            """
            while total(user_hand) < 21:
                repeat = input(" Your hand is now ", total(user_hand), " would you like to hit again? (Yes/No) \n").lower()
                if repeat == "yes":
                    hit(user_hand)
            evaluate(dealer_hand, user_hand)
            """
            again()
        elif choice == "stay":
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            evaluate(dealer_hand, user_hand)
            again()
        elif choice == "quit":
            print("Good Bye! Hope you liked it")
            exit()
     

main()