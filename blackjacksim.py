####################################################
####################################################
######## GAMBA SIMULATOR V3: BLACKJACK SIM #########
####################################################
####################################################




import os
import random
import sys
import time

card_type = "Hearts","Spades","Diamonds","Clubs"
card_value = "2","3","4","5","6","7","8","9","10","Ace","King","Jack","Queen"



player_hand = []
dealer_hand = []

player_points = sum(points_system(card) for card in player_hand)
dealer_points = sum(points_system(card) for card in dealer_hand)
real_points = 0
hands_played = 0
bet_dd = 0

rank = ""
suit = ""

def hud():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Dealer hand:")
    print_card(dealer_hand)
    print(f"Dealer points: {dealer_points}")
    print("")
    print(f"=====| Hands played: xxx |=======| Bankroll: ${current_money} |=====")
    print(f"\nPlayer hand:")
    print_card(player_hand)
    print(f"Player points: {player_points}")
    print("")
    
    
money = 250
current_money = money
    
    
    
    
    

def create_card(card):
    rank, suit = card
    suit_symbols = {"Hearts":"♥", "Diamonds":"♦", "Clubs":"♣", "Spades":"♠"}
    rank_symbols = {"2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10","Ace":"A","King":"K","Jack":"J","Queen":"Q"}
    s = suit_symbols[suit]
    r = rank_symbols[rank]
    
    
    
    return [
        f"┌─────────┐",
        f"│{r:<2}       │",
        f"│         │",
        f"│         │",
        f"│    {s}    │",
        f"│         │",
        f"│         │",
        f"│       {r:>2}│",
        f"└─────────┘"
    ]

    
def print_card(hand):
    if not hand or len(hand) == 0:
        print("(no cards)")
        return
    card_lines = [create_card(card) for card in hand]
    
    for i in range(len(card_lines[0])):
        print(" ".join(card[i] for card in card_lines))
    

def game_logic():
    while current_money > 0:
        print("================================")
        print("======= Author: Amin H. ========")
        print("================================")

        start_quit = input("Welcome to blackjack! Start (S) or Quit (Q)").upper()
        if start_quit == "S":
            print("Shuffling deck...")
            time.sleep(0.5)
            print("Distributing cards...")
            time.sleep(0.5)
            start()
        elif start_quit == "Q":
            print("Quitting game...")
            sys.exit()
            
    else:
        print("You've lost all your money!")
        game_restart()
   
        
   
    
     
def start():
    global dealer_points, player_points, bet, current_money  
    hand_reset()
    bet = betAmount()
    initial_draw()
    print(f"You bet ${bet}")
    while player_points < 21:

        hit_or_stand = input("Hit (H), Stand (S) or Double-down (D)?").upper()
        
        if hit_or_stand == "H":
            player_deal()
            print("Drawing card...")
            time.sleep(0.5)
            hud()
            player_points = sum(points_system(card[0]) for card in player_hand)
            
            if player_points > 21:
               print("Bust! You lose.")
               game_restart()
               break
           
        elif hit_or_stand == "S":
            round_game()
            money_check()
            
        elif hit_or_stand == "D":
            double_down()
            
            if player_points > 21:
                print("Bust! You lose.")
                game_restart()
                
            elif player_points < 21:
                continue
            else:
                round_game()
                money_check()
        else:
              ("Invalid choice: Press (H) or (S)")
                 
def round_game():
    
    while 21 > dealer_points <= 16:
        dealer_deal()
        time.sleep(0.5)
        hud()

                 
    if dealer_points > 21:
        print("Dealer BUST! You win.")
        isWin()
        game_restart()
        
        
                 
    elif player_points < dealer_points:
        print(f"You lose! Dealer had {dealer_points} to your {player_points}")
        game_restart()

                 
    elif player_points == dealer_points:
        print("Draw!")
        isDraw()
        game_restart()

                     
    else:
        isWin()
        hud()
        print(f"You win! You had {player_points} to dealer's {dealer_points}")
        game_restart()

    
                
def hand_reset():
    global dealer_points, player_points
    player_hand.clear()
    dealer_hand.clear()
    player_points = 0
    dealer_points = 0
    hud()
        
def initial_draw():
    dealer_deal()
    print("Drawing card...")
    time.sleep(0.5)
    hud()
    dealer_deal()
    print("Drawing card...")
    time.sleep(0.5)
    hud()
    player_deal()
    print("Drawing card...")
    time.sleep(0.5)
    hud()
    player_deal()
    print("Drawing card...")
    time.sleep(0.5)
    hud()


def player_deal():
    global player_points
    card = draw_card()
    player_hand.append(card)
    player_points += points_system(card[0])
       
    
def dealer_deal():
    global dealer_points
    card = draw_card()
    dealer_hand.append(card)
    dealer_points += points_system(card[0])


def draw_card():
    rank = random.choice(card_value)
    suit = random.choice(card_type)
    return (rank, suit)


def points_system(rank):
    if rank in ["King","Queen","Jack"]:
        return 10
    elif rank == "Ace":
        if player_points > 11:
            return 1
        else:
            return 11
    else:
        return int(rank)
        
    
def game_restart():
    money_check()
    while True:
        restart_quit = input("Restart (S) or Quit (Q):").upper()
        if restart_quit == "S":
            print("Starting new game...")
            start()
        elif restart_quit == "Q":
            sys.exit()
    else:
        print("Invalid input! Press (S) or (Q)")
        



def double_down():
    global current_money, bet_dd
    if current_money > 0:
        bet_dd = 0
        bet_dd = bet*2
        current_money = current_money - bet
        player_deal()
        hud()
        print(f"You double down! Your bet is now {bet_dd}")
    else:
        print("You dont have enough money!")
        
    
    

    

def isWin():
    global current_money
    if bet_dd > 0:
        current_money = current_money + bet_dd + bet*2
    else:
        current_money = current_money + bet*2


    
def isDraw():
    global current_money
    current_money = current_money + bet

def money_check():
    while current_money < 1:
        r_or_q = input("You've run out of money! Restart (R) or Quit (Q)").upper()
        if r_or_q == "R":
            full_restart()
        elif r_or_q == "Q":
            sys.exit()
        else:
            print("Invalid input.")
        
        
        
def full_restart():
    global current_money
    current_money = money
    hud()
    

def betAmount():
    global current_money
    money_check()
    hud()
    bet = 0
    while True:
        bet = input("Place your bet: $")
        if not bet.isdigit():
            print("Invalid! it has to be a number")
            continue
        bet = int(bet)
            
        if bet <= 0:
            print("Invalid! You have to bet more than $1")
            continue
        
        if bet > current_money:
            print("Invalid! You dont have that much.")
            continue
            
        else:
            bet = int(bet)
            print(f"You bet ${bet}")
            current_money = current_money - bet
    
            return bet



game_logic()




