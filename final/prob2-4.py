import random as rd

player_hand = list()
dealer_hand = list()  
hand = list()
player = list()
handnum = list()
plusnum = list()
bat = list()
total_bat = list()

print("\t\t\tWelcome to Blackjack!\n\n")

players = input("How many players? <1 - 7>: ")
for i in range(int(players)):
    player_name = input("Enter player name: ")
    player.append(player_name)
    total_bat.append(10)

def randhand():
    rdCard = rd.randrange(0, len(Card))
    player_hand.append(Card[rdCard])
    Card.pop(rdCard)

def plus10(hand):
    tmp = 0
    for card in hand:
        if card[0] in ['J', 'Q', 'K', 'A']:
            tmp += 10
        else:
            tmp += int(card[:-1])
    return tmp

def numhand():
    for ph in hand:
        player_hand_num = [card[:-1] for card in ph]
        handnum.append(player_hand_num)

def compare_hands(player_total, dealer_total):
    if player_total > 21:
        return "Busts!"
    if dealer_total > 21:
        return "wins."
    elif player_total == dealer_total:
        return "Draw!"
    elif player_total > dealer_total:
        return "wins."
    else:
        return "loses."

while True:
    Card = ["Ac", "2c", "3c", "4c", "5c", "6c", "7c",
        "8c", "9c", "10c", "Jc", "Qc", "Kc",
        "Ad", "2d", "3d", "4d", "5d", "6d", "7d",
        "8d", "9d", "10d", "Jd", "Qd", "Kd",
        "Ah", "2h", "3h", "4h", "5h", "6h", "7h",
        "8h", "9h", "10h", "Jh", "Qh", "Kh",
        "As", "2s", "3s", "4s", "5s", "6s", "7s",
        "8s", "9s", "10s", "Js", "Qs", "Ks"]
        
    player_hand = []
    dealer_hand = []  
    hand = []
    handnum = []
    plusnum = []
    bat = []
        
    for i in range(int(players)):
        tmp = input(f"{player[i]}, How much will you bat($)? : ")
        bat.append(tmp)
        
    for j in range(0, int(players) + 1):
        player_hand = []
        for k in range(0, 2):
            randhand()
        if j == int(players):  
            dealer_hand = player_hand.copy()
        else:
            hand.append(player_hand)

    numhand()

    for i in range(int(players)):
        print(player[i], ":\t", *hand[i], "\t", "(", plus10(hand[i]), ")\ttotal $ = ", total_bat[i], "\tbat($)=", bat[i])
    print("Dealer:\t", "XX", *dealer_hand[1:], "\n")

    for i in range(int(players)):
        re = input(f"{player[i]} do you want a hit? (y/n): ")
        while re == 'y':
            randhand()
            hand[i].append(player_hand[-1])
            print(player[i], ":\t", *hand[i], "\t", "(", plus10(hand[i]), ")\n")
            if plus10(hand[i]) > 21:
                break
            re = input(f"{player[i]} do you want another hit? (y/n): ")

    while plus10(dealer_hand) < 17:
        randhand()
        card = Card[-1]
        dealer_hand.append(card)
        Card.remove(card)

    print("Dealer:", *dealer_hand, "\t", "(", plus10(dealer_hand), ")\n")

    for i in range(int(players)):
        result = compare_hands(plus10(hand[i]), plus10(dealer_hand[1:]))
        if result == "win":
            total_bat[i] += int(bat[i])*2
        elif result == "Busts!" or result == "loses.":
            total_bat[i] -= int(bat[i])
        print(f"{player[i]} {result} $ : {total_bat[i]}")
    
    again = input("Do you wnat to play again? (y/n):")
    if again == 'n':
        break
