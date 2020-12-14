"""

First we need the deck of cards
Deck = list that that contains numbers 2-14 * 4 for number of suits in a deck
set if statements where 11 = Jack, 12 = Queen, 13 = King, Ace = 1 or 11 
Jack, Queen, King = 10 to points
Ace = 1 or 11 depending if the total goes over 21
Shuffle deck, show dealers hand of 1 card and one unknown
Show users hand of 2 known cards 
Ask if they want another card through "Hit" or to keep what they have, "Stay"
Once user input is finished Deal the dealers hands, if dealerTotal < 16, else dealer stays on 17 to 21
After Dealer and User are done being dealt cards, compare the 2, higher number wins
If dealer or User go over 21 they lose
if compared and they equal, Game = draw
if dealer > user, dealer wins, while under 21
if user > dealer user wins, while under 21
"""