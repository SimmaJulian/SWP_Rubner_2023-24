  
    
import random

def who_wins(player, pc):
    if player == 'scissors' and pc == 'paper' or pc == 'lizard':
        return 'player'
    elif pc == 'scissors' and player == 'paper' or player == 'lizard':
        return 'pc'
    
    elif player == 'paper' and pc == 'rock' or pc == 'spock':
        return 'player'
    elif pc == 'paper' and player == 'rock' or player == 'spock':
        return 'pc'

    
    elif player == 'rock' and pc == 'lizard' or pc == 'scissors':
        return 'player'
    elif pc == 'rock' and player == 'lizard' or player == 'scissors':
        return 'pc'

    
    elif player == 'lizard' and pc == 'spock' or pc == 'paper':
        return 'player'
    elif pc == 'lizard' and player == 'spock' or player == 'paper':
        return 'pc'
     
    
    elif player == 'spock' and pc == 'scissors' or pc == 'rock':
        return 'player'
    elif pc == 'spock' and player == 'scissors' or player == 'rock':
        return 'pc'
    
    return 'draw'

def player_choice():
    while (True):
        print("\n--------------------------------------------------------------")
        print("Rock     = 0")
        print("Lizard   = 1")
        print("Spock    = 2")
        print("Scissors = 3")
        print("Paper    = 4")
        print("Eingabe: ")
        my_in = input()
    
        try:
            ret_choice_player = int(my_in)
        except ValueError:
            print("incorrect input")
        else:
            if ret_choice_player >= 0 and ret_choice_player < 5:
                return ret_choice_player
            else:
                print("incorrect input")   

def player_choice_string(choise):
    
    if choise == 0:
        return 'rock' 
    if choise == 1:
        return 'lizard'
    if choise == 2:
        return 'spock'
    if choise == 3:
        return 'scissors'
    if choise == 4:
        return 'paper'


def game_continue():        
    while(True):
        print("\nWeiter spielen?")
        print("Ja...........j")
        print("Nein.........n")
        my_in = input()
        
        if my_in == 'j':
            return True
        elif my_in == 'n':
            return False
        else:
            print("incorrect input")

def save_into_dict(my_dictionary, name):
    my_dictionary[name] = my_dictionary.get(name, 0) + 1

def get_dict_value(my_dictionary, name):
    return my_dictionary.get(name, 0)

def get_dicts():
    wins = {'draw': 0, 'player': 0, 'pc': 0}
    player_symbols = {'rock': 0, 'lizard': 0, 'spock': 0, 'scissors': 0, 'paper': 0}
    ai_symbols = {'rock': 0, 'lizard': 0, 'spock': 0, 'scissors': 0, 'paper': 0}
    return wins, player_symbols, ai_symbols

def menu():
    while (True):
        print("---------------------------")
        print("Spielen.......0")
        print("Statistik.....1")
        print("Beenden.......2")
        print("Choose!")
        my_in = input()
    
        try:
            menu_select = int(my_in)
        except ValueError:
            print("incorrect input")
        else:
            if menu_select == 0:
                return 'RPSSL' 
        
            elif menu_select == 1:
                return 'statistics'

            elif menu_select == 2:
                return 'quit'
        
            else:
                print("incorrect input")
            
    return menu_select

def statistics(win, player_selections, pc_selections):
    print("----------------------------------")
    print("Wins:")
    for w in win:
        print(w + " = " + str(win[w]))   

    print("\nSpieler Auswahlen:")
    for p in player_selections:
        print(p + " = " + str(player_selections[p]))   

    print("\nPC Auswahlen:")
    for a in pc_selections:
        print(a + " = " + str(pc_selections[a]))   

if __name__ == '__main__':
    win_dict, player_dict, ai_dict = get_dicts()

    while True:
        main_menu_option = menu()

        if main_menu_option == 'RPSSL':
            continue_playing = True
            while continue_playing:
                player_choice_str = player_choice_string(player_choice())
                ai_choice_str = player_choice_string(random.randint(0, 4))

                save_into_dict(player_dict, player_choice_str)
                save_into_dict(ai_dict, ai_choice_str)

                result = who_wins(player_choice_str, ai_choice_str)
                save_into_dict(win_dict, result)

                print('\n' + player_choice_str + ' --- ' + ai_choice_str)
                print(result + " wins!\n")

                continue_playing = game_continue()

        if main_menu_option == 'statistics':
            statistics(win_dict, player_dict, ai_dict)

        if main_menu_option == 'quit':
            break
