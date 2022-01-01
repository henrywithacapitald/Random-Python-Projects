

import random

def main():
    user_name = "" #Add your username here
    player_wins = 0
    computer_wins = 0
    draws = 0
    player_selection = 1
    display_banner(user_name)
    while player_selection != 0:
        print()
        display_menu()
        player_selection = get_user_input()
        if player_selection == 1:
            player_roll = get_valid_roll()
            computer_roll = get_valid_roll()
            player_score = get_score(player_roll)
            computer_score = get_score(computer_roll)
            print()
            print_separator()
            print_roll("Player", player_roll, player_score)
            print_roll("Computer", computer_roll, computer_score)
            if player_score > computer_score:
                print("Player has won!")
                player_wins += 1
            elif player_score < computer_score:
                print("Computer has won!")
                computer_wins += 1
            else:
                print("It's a draw!")
                draws += 1
            print("Player wins:", player_wins, "Computer wins:", computer_wins, "Draws:", draws)
            print_separator()
    print()
    print_separator()
    print_player_stats(player_wins, computer_wins, draws)
    print_separator()
        
#Paste your completed functions here
   
main()
    
        
