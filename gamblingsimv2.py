####################################################
####################################################
############# BETTING SIMULATOR 2025 ###############
####################################################
####################################################


import random
import sys
import os
import time

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[0;36m"
RESET = "\033[0m"


money = 250
total_winnings = 0
current_money = money
total_wins = 0

print("==========================")
print("============= RULES ===================")
print("|1. If you run out of money, you lose.|")
print("|2. Difficulty multimpliers:          |")
print("|3.   Easy: 10 Guesses, 1.5x return   |")
print("|4.   Normal: 5 Guesses, 5x return    |")
print("|5.   Hard: 3 Guesses, 7x return      |")
print("|6.   Impossible: 1 Guess, 20x return |")
print("=======================================")


def hud():

    os.system('cls' if os.name == 'nt' else 'clear')
    

    print(f"{YELLOW}============ STATS ============")
    print(f"Money: {GREEN}${current_money}{YELLOW}")
    print(f"{YELLOW}Total wins: {BLUE}{total_wins}{YELLOW}")
    print(f"Total winnings: {GREEN}${total_winnings}{YELLOW}")
    print(f"{YELLOW}===============================\n{RESET}")

def betAmount():
    global current_money
    bet = 0
    while True:
        bet = int(input(f"Place your bet: $"))
        if bet < 1:
            print("You cant bet for free!")
        elif bet > current_money:
            print("You dont have that much money!")
        else:
            current_money = current_money - bet
            hud()
            print(f"You bet ${bet}, good luck!")
            return bet    
    
def g_logic():
    hud()
    start_quit = input(f"{BLUE}Press Start (S) or Quit (Q) to continue!{RESET} ").upper()
    while start_quit != "S" and start_quit != "Q":
        start_quit = input(f"{YELLOW} Invalid input. Please choose Start (S) or Quit (Q) to continue...").upper()
        
    if start_quit == "S":
        print(f"{BLUE} Starting game...")
        s_game()
        
    elif start_quit == "Q":
        print(f"{BLUE} Shutting down game...")


    
def s_game():
    global current_money
    global total_winnings
    global total_wins
    bet = betAmount()
    total_tries = choose_difficulty()
    attempts = 0
    gen_int = random.randint(1, 100)
    
   # print(gen_int) ## use to test if working.
    
    while attempts < total_tries:
        user_int = input(f"{BLUE} Guess a number between 1-100!: {RESET}")
        
        if not user_int.isdigit():
            print(f"{YELLOW}'{user_int}' is not a number! Please type a number between 1-100.{RESET} ")
            continue
            
        else: user_int = int(user_int)

        if user_int > 100:
            print(f"{YELLOW}Invalid: Number is higher than 100! Please enter a number between 1-100!{RESET} ")
            continue
        
        elif user_int < 1:
            print(f"{YELLOW}Invalid: Number is lower than 1! Please enter a number between 1-100!{RESET} ")
            continue
        
        attempts = attempts + 1
        tries_left = total_tries - attempts
        
        if user_int == gen_int:
            
            if difficulty ==1:
                winnings = bet*1.5
            elif difficulty == 2:
                winnings = bet*3
            elif difficulty == 3:
                winnings = bet*7
            elif difficulty == 4:
                winnings = bet*20
                
            current_money = current_money + winnings
            total_winnings = total_winnings + winnings
            total_wins = total_wins + 1
            hud()
            print(f"{BLUE}Congratulations! {GREEN}{user_int}{BLUE} is the correct number! {RESET}")
            print(f"{GREEN} +${winnings} {RESET}")
            restart()
            
        elif user_int > gen_int:
            print(f"{RED} {user_int}{RESET} {BLUE}is too {RED}HIGH!{BLUE} You have {RESET}{RED}{tries_left}{BLUE} guesses remaining!")
            
        elif user_int < gen_int:
            print(f"{RED} {user_int}{RESET} {BLUE}is too {RED}LOW!{BLUE} You have {RESET}{RED}{tries_left}{BLUE} guesses remaining!")
            
    else:
        print(f"{BLUE} You have {RED}0{BLUE} remaining guesses, The correct number was {GREEN}{gen_int}.{RESET}")
        print(f"{RED} -${bet}{RESET}")
        if current_money > 0:
            restart()
        else:
            print("GG You're out of money:(")
            print("Shutting down game...")
            sys.exit()
  
    
def restart():
    restart = input(f"{BLUE}Press (S) to restart or (Q) to quit. ").upper()
    while restart != "S" and restart != "Q":
        restart = input(f"{YELLOW} Invalid option. Please choose (S) or (Q){BLUE}").upper()
        
    if restart == "S":
        print(f"{BLUE} Restarting game...")
        s_game()
        
    elif restart == "Q":
        print(f"{BLUE} Shutting down game...")
        sys.exit()
    
    
def choose_difficulty():
    global difficulty
    while True:
        difficulty = int(input("Choose difficulty: Easy (1), Normal (2), Hard (3) or Impossible (4): ")) 
        if difficulty == 1:
           total_tries = 10
        
        elif difficulty == 2:
           total_tries = 5
        
        elif difficulty == 3:
           total_tries = 3
        
        elif difficulty == 4:
           total_tries = 1
        else:
           print("Invalid! Pick a difficulty 1-4")
        return total_tries


g_logic()

