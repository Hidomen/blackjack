import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

data = {
        "player" : {
            "hand" : [],
            "score" : 0
        },

        "dealer" : {
            "hand" : [],
            "score" : 0
        }
} 

def main():
#-       starting of game        -
    data["player"]["hand"].extend([deal(), deal()])
    data["dealer"]["hand"].extend([deal(), deal()])
    
    while total_calc(data["player"]["hand"]) <= 21:
        gui(data)

        if total_calc(data["player"]["hand"]) == 21:
            game_over("player")
            break
        else:
            choice = input("Do you want to draw?: ").upper()
            if choice == "Y":
                data["player"]["hand"].append(deal())

            elif choice == "N":
                if total_calc(data["dealer"]["hand"]) < 17:
                    data["dealer"]["hand"].append(deal())
                break
            else:
                print("Invalid option")

    # when its finished
    gui(data)

    player_total = total_calc(data["player"]["hand"])
    dealer_total = total_calc(data["dealer"]["hand"])
    if player_total > 21:
        game_over("dealer")
    elif player_total > dealer_total:
        if player_total <= 21:
            game_over("player")
        else:
            game_over("dealer")
    elif player_total < dealer_total:
        if dealer_total <= 21:
            game_over("dealer")
        else:
            game_over("player")
    elif player_total == dealer_total and dealer_total <= 21 and player_total <= 21:
        game_over("draw")
    else :
        # just in case for bugs
        print(player_total, dealer_total)
        print("114")
    
    # play again:--
    while True:
        again = input("wanna play again? (Y/N): ").upper()
        if again == "Y":
            data["player"]["hand"] = []
            data["dealer"]["hand"] = []
            main()
            break
        elif again == "N":
            print(f'YOUR SCORE: {data["player"]["score"]}')
            print(f"DEALER'S SCORE: {data['dealer']['score']}")
            break
        else:
            print("INVALID OPTION")
    

def deal():
    clones = [10, "J", "Q", "K"]

    card = int(random.choice(cards))
    if card == 10:
        card = random.choice(clones)
        

    return card


def total_calc(hand): 
    royals = ["J", "Q", "K"]
    total = 0

    for card in hand:
        if card in royals:
            total += 10
        else:
            total += card
    
    if 11 in hand and total > 21:
        total -= 10

    return total


def gui(data):

    print("***************")
    print(f"YOUR HAVE: ", end="")
    for card in data["player"]["hand"]:
        if card != 11:
            print(f"{card}", end=" ")
        else:
            print("1", end=" ") 

    print(f'\ntotal is {total_calc(data["player"]["hand"])}\n\n')
    if data["dealer"]["hand"][0] == 11:
        print(f'DEALER HAS: 1')
    else:
        print(f'DEALER HAS: {data["dealer"]["hand"][0]}')
    print(data["dealer"]["hand"], total_calc(data["dealer"]["hand"])) # for bug-fixes
    print("***************")
     
    
def game_over(winner):
    if winner == "player":
        print("HEY YOU WON MAN!!!")
        data["player"]["score"] += 1

    elif winner == "dealer":
        print("loSEr")
        data["dealer"]["score"] += 1
    else :
        print("ITS A TIE")

    
    print("\n\nDEALER HAD: ")
    for card in data["dealer"]["hand"]:
        if card != 11:
            print(card, end=" ")
        else:
            print(1, end=" ")
    print(f'-- TOTAL OF {total_calc(data["dealer"]["hand"])}\n\n')
main()