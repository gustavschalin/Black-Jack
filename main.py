import random

 # Locked or Unlocked
achieve1 = 0
achieve2 = 0
achieve3 = 0


 # Dealer cards
dealer_cards = []

 # Player cards
player_cards = []

def main():
    main_menu()
    choice()

 # Main Menu
def main_menu():
    print("" * 20)
    print("/" * 20)
    print("\033[01;34mStart Game: Type A\033[01;37m")
    print("\033[01;32mAchievement: Type B\033[01;37m")
    print("\033[01;31mExit: Type C\033[01;37m")
    print("/" * 20)

 # Make a choice
def choice():
    player_choice = input("\033[01;35mChoose Statment:\033[01;37m ").upper()
    if player_choice == "A":
        first_statment()
        choice()
    elif player_choice == "B":
        achievement()
        choice()
    elif player_choice == "C":
        print("CYA!!!")
        pass
    else:
        print("Choose the right choice to continue")


 # Achievements
def achievement():
    print("" * 20)
    print("Achievements Locked and Unlocked")
    print("*" * 20)
    if achieve1 == True:
        print("Smart Ass: " + "\033[01;32mUnlocked\033[01;37m")
        print("Use your mind to win over the Dealer")
        print("" * 20)
    elif achieve1 == False:
        print("Smart Ass: " + "\033[01;31mLocked\033[01;37m")
        print("Use your mined to win over the Dealer")
        print("" * 20)
    if achieve2 == True:
        print("BUSTED: " + "\033[01;32mUnlocked\033[01;37m")
        print("Lose a game against the Dealer")
        print("" * 20)
    elif achieve2 == False:
        print("BUSTED: " + "\033[01;31mLocked\033[01;37m")
        print("Lose a game against the Dealer")
        print("" * 20)
    if achieve3 == True:
        print("Champion VS Champion: " + "\033[01;32mUnlocked\033[01;37m")
        print("Get a tie with the dealer")
        print("" * 20)
    elif achieve3 == False:
        print("Champion VS Champion: " + "\033[01;31mLocked\033[01;37m")
        print("Get a tie with the dealer")
    print("*" * 20)

 # Showing Cards
def first_statment():
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print("Dealer has: X &", dealer_cards[1])
    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 11))
        if len(player_cards) == 2:
            print("You have:", player_cards)
            busted()

 # Busted - If you get Black Jack or Busted immediately
def busted():
    if sum(dealer_cards) > 21:
        achieve1 = True
        print("Dealer Cards " + str(sum(dealer_cards)))
        print("You have a total of: " + str(sum(player_cards)))
        print("Dealer has busted, You Win!")
        main_menu()
        choice()

    elif sum(player_cards) > 21:
        achieve2 = True
        print("Dealer Cards " + str(sum(dealer_cards)))
        print("You have a total of: " + str(sum(player_cards)))
        print("You have busted, Dealer Win!")
        main_menu()
        choice()

    if sum(dealer_cards) == 21:
        achieve2 = True
        print("Dealer Cards " + str(sum(dealer_cards)))
        print("You have a total of: " + str(sum(player_cards)))
        print("Dealer have Black Jack!, Dealer Win")
        main_menu()
        choice()

    elif sum(player_cards) == 21:
        achieve1 = True
        print("Dealer Cards " + str(sum(dealer_cards)))
        print("You have a total of: " + str(sum(player_cards)))
        print("You got BLACK JACK, You Win!")
        main_menu()
        choice()

    action()

 # Stay or Hit -
def action():
    while sum(player_cards) < 21:
        action_taken = input("Stay or Hit?: ").lower()
        if action_taken == "hit":
            player_cards.append(random.randint(1, 11))
            print("You have a total of: " + str(player_cards), sum(player_cards))
        elif action_taken == "stay":
            end()
            break
    if sum(dealer_cards) > 21:
        achieve1 = True
        print("Dealer Cards " + str(sum(dealer_cards)))
        print("You have a total of: " + str(sum(player_cards)))
        print("Dealer has busted, You Win!")
        main_menu()
        choice()

    elif sum(player_cards) > 21:
        achieve2 = True
        print("Dealer Cards " + str(sum(dealer_cards)), dealer_cards)
        print("You have a total of: " + str(sum(player_cards)))
        print("You have busted, Dealer Win!")
        main_menu()
        choice()
    if sum(dealer_cards) == 21:
        achieve2 = True
        print("Dealer Cards " + str(sum(dealer_cards)))
        print("You have a total of: " + str(sum(player_cards)))
        print("Dealer have Black Jack!, Dealer Win")
        main_menu()
        choice()

    elif sum(player_cards) == 21:
        achieve1 = True
        print("Dealer Cards " + str(sum(dealer_cards)))
        print("You have a total of: " + str(sum(player_cards)))
        print("You got BLACK JACK, You Win!")
        main_menu()
        choice()

 # Compare which one wins - Gives Dealer new cards - And ends program
def end():
    while sum(dealer_cards) <= 17:
        dealer_cards.append(random.randint(1, 11))
        if sum(dealer_cards) > 17:
            break
    print("Dealers Cards: " + str(sum(dealer_cards)))
    print("You have a total of: " + str(sum(player_cards)))

    if sum(dealer_cards) > 21:
        achieve1 = True
        print("Dealer has busted, You Win!")
        main_menu()
        choice()

    elif sum(player_cards) > 21:
        achieve2 = True
        print("You have busted, Dealer Win!")
        main_menu()
        choice()

    if sum(dealer_cards) > sum(player_cards):
        achieve2 = True
        print("Dealer Wins, You lose :(")
        main_menu()
        choice()

    elif sum(player_cards) > sum(dealer_cards):
        achieve1 = True
        print("You Win!, Dealer lose :)")
        main_menu()
        choice()

    if sum(player_cards) == sum(dealer_cards):
        achieve3 = True
        print("It's a Tie, No one wins")
        main_menu()
        choice()

main()
