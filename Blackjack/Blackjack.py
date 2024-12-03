import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def card() :
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
while True :
    init_call = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if init_call == 'n' :
        break
    print("\n" * 20)
    print(art.logo)
    player_cards = []
    player_cards.append(card())
    player_cards.append(card())
    dealer_cards = []
    dealer_cards.append(card())
    dealer_cards_hidden = dealer_cards
    dealer_cards_hidden.append(card())
    dealer_score = sum(dealer_cards_hidden)
    player_score = sum(player_cards)
    if player_cards.count(11) == 2 :
        player_score -= 10
    while  dealer_score < 16 :
        dealer_cards_hidden.append(card())
        dealer_score=sum(dealer_cards_hidden)
    if 11 in dealer_cards_hidden :
        if dealer_score > 21 :
            dealer_score -= 10
    flag = 0
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {dealer_cards[0]}")
    while True :
        next_call = input("Type 'y' to get another card, type 'n' to pass: ")
        if next_call == 'y' :
            player_cards.append(card())
            player_score = sum(player_cards)
        if player_cards.count(11) == 2:
            player_score -= 10
        if player_cards.count(11) > 2 :
            player_score -= 10*(player_cards.count(11)-1)
        if player_cards.count(11) == 1 and player_score > 21 :
            player_score -= 10
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")
        if player_score > 21 :
            flag = 1
            break
        elif next_call == 'n' :
            flag = -1
            break
    if flag == 1 :
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {dealer_cards_hidden}, final score: {dealer_score}")
        print("You lose")
    if flag == -1 :
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {dealer_cards_hidden}, final score: {dealer_score}")
        if player_score > dealer_score :
            print("You win")
        elif player_score < dealer_score :
            print("You lose")
        else :
            print("Draw")

