import os
import random
def output_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def before_start():
    global is_bot
    print('\nWelcome to the TicTacToe game!\n')
    while True:
        first_input = input('To play the game with the Bot, enter number 1.\nTo play with your friend, enter number 2.\nIf you want to know about the game instructions enter help: ')
        output_cleaner()
        if first_input.lower() == '2':
            output_cleaner()
            is_bot = False
            print('Game started!\n')
            break
        elif first_input.lower() == '1':
            output_cleaner()
            print('Game started!\n')
            is_bot = True
            break
        elif first_input.lower() == 'help':
            output_cleaner()
            print('When the game starts, you should enter one of these numbers to mark that block with your sign.\n')
            print('1','|','2','|','3')
            print('---------')
            print('4','|','5','|','6')
            print('---------')
            print('7','|','8','|','9\n')
            print("Player 1's sign is X, and Player 2's sign is O.")
        else:
            output_cleaner()
            print('Wrong input! Try again.')

def sign_chooses():
    if is_bot == True:
        while True:
            player_1_sign = input('With which sign do you want to play? X or O: ').lower()
            if player_1_sign == 'x' or player_1_sign == 'o':
                output_cleaner()
                break
            else:
                output_cleaner()
                print('Player 1, you did not enter X or O! Try again.')
        player_2_sign = ['x', 'o']
        player_2_sign.remove(player_1_sign)
        player_2_sign = player_2_sign[0]
        return [player_1_sign, player_2_sign]

    while is_bot != True:
        while True:
            player_1_sign = input('Player 1, with which sign do you want to play? X or O: ').lower()
            if player_1_sign == 'x' or player_1_sign == 'o':
                output_cleaner()
                break
            else:
                output_cleaner()
                print('Player 1, you did not enter X or O! Try again.')
        
        while True:
            player_2_sign = input('Player 2, with which sign do you want to play? X or O: ').lower()
            if player_2_sign == 'x' or player_2_sign == 'o':
                break
            else:
                output_cleaner()
                print('Player 2, you did not enter X or O! Try again.')

        if (player_1_sign == 'x' and player_2_sign == 'x') or (player_1_sign == 'o' and player_2_sign == 'o'):
            output_cleaner()
            print('Because you both picked the same sign, I will randomly assign you a sign to play with!')
            while True:
                player_1_sign = random.choice(['x','o'])
                player_2_sign = random.choice(['x','o'])
                if player_1_sign != player_2_sign:
                    break
            if player_1_sign == 'x':
                print('Player 1, you will play with the sign X!')
                print('Player 2, you will play with the sign O!')
                print('\n')
                return [player_1_sign, player_2_sign]
            elif player_1_sign == 'o':
                print('Player 1, you will play with the sign O!')
                print('Player 2, you will play with the sign X!')
                print('\n')
                return [player_1_sign, player_2_sign]
        elif player_1_sign == 'x' and player_2_sign == 'o':
            output_cleaner()
            print('Player 1 has chosen the sign X!')
            print('Player 2 has chosen the sign O!')
            print('\n')
            break
        elif player_1_sign == 'o' and player_2_sign == 'x':
            output_cleaner()
            print('Player 1 has chosen the sign O!')
            print('Player 2 has chosen the sign X!')
            print('\n')
            break
    return [player_1_sign, player_2_sign]

def player_turn(player, sign, player1_detect = 0, player2_detect = 0, is_bot = False):
    if player1_detect == 1:
        n = 1
    elif player2_detect == 2:
        n = 2  
    elif is_bot == True:
        n = 3

    while True:
        if is_bot == True:
            if n == 1:
                while True:
                    player = input(f'Which block do you want to mark? ')
                    if player.isdigit() and 1<=int(player)<=9 :
                        player = int(player)
                        break
                    else:
                        output_cleaner()
                        print(f'You did not enter an integer number between 1 and 9! Try again.\n')
                        signed_block_displayer()
            else:
                print('Bot’s move:')
                signs = ['X','O']
                signs.remove(sign)
                player_sign = signs[0]

                player_flag = 0
                for a, b, c in win_patterns:
                    count = 0
                    for d in [a,b,c]:
                        if x_list[d-1] == player_sign:
                            count += 1

                    if count == 2:
                        for d in [a,b,c]:
                            if x_list[d-1] == ' ':
                                player_flag = 1
                                player = d
                                break
                    if player_flag == 1:
                        break

                bot_flag = 0
                for a, b, c in win_patterns:
                    count = 0
                    for d in [a,b,c]:
                        if x_list[d-1] == sign:
                            count += 1

                    if count == 2:
                        for d in [a,b,c]:
                            if x_list[d-1] == ' ':
                                bot_flag = 1
                                player = d
                                break
                    if bot_flag == 1:
                        break

                if bot_flag != 1 and player_flag != 1:
                    player = random.randint(1,9)

                
        else:
            if n != 3:
                while True:
                    player = input(f'Player {n}, which block do you want to mark? ')
                    if player.isdigit() and 1<=int(player)<=9:
                        player = int(player)
                        break
                    else:
                        output_cleaner()
                        print(f'Player {n}, you did not enter an integer number between 1 and 9! Try again.\n')
                        signed_block_displayer()
        if bot_playing_first != 1:
            output_cleaner()

        if player not in used_blocks:
            used_blocks.add(player)
            x_list[player-1] = sign
            break
        else:
            output_cleaner()
            print(f'Player {n}, the block you chose is full! Try again.\n')
            signed_block_displayer()
    return True

def signed_block_displayer():
    print(f'{x_list[0]} | {x_list[1]} | {x_list[2]}')
    print('---------')
    print(f'{x_list[3]} | {x_list[4]} | {x_list[5]}')
    print('---------')
    print(f'{x_list[6]} | {x_list[7]} | {x_list[8]}\n')

def final_result(final_result_var_player1, final_result_var_player2):
    final_result_var_list = [final_result_var_player1, final_result_var_player2]
    for sign in final_result_var_list:
        for a,b,c in win_patterns:
            if x_list[a-1] == x_list[b-1] == x_list[c-1] == sign:
                output_cleaner()
                print('Game ended!\n')
                signed_block_displayer()
                if is_bot == True:
                    print('You won! :)' if sign == final_result_var_list[0] else 'You lost! :(')
                else:
                    if sign == final_result_var_list[0]:
                        print('Player 1, you won! ;)')
                        print('Player 2, you lost :(')
                    else:
                        print('Player 2, you won! ;)')
                        print('Player 1, you lost :(')
                return True
    if all(x != ' ' for x in x_list):
        output_cleaner()
        print('The game ended in a tie!\n')
        signed_block_displayer()
        return True

def play_again():
    while True:
        player_answer = input('\nDo you want to play again? Enter Yes or No: ').lower()
        output_cleaner()
        if player_answer == 'yes':
            return True
        elif player_answer == 'no':
            return False
        else:
            print('You did not enter yes or no! Try again!')
        
def combined_fun_p1():
    player1 = None    
    player_turn(player1, sign_chooses_var[0].upper(), 1)
    signed_block_displayer()
    return final_result(sign_chooses_var[0].upper(), sign_chooses_var[1].upper())

def combined_fun_p2():
    player2 = None
    if is_bot == False:
        player_turn(player2, sign_chooses_var[1].upper(), 0, 2)
    elif is_bot == True:
        player_turn(player2, sign_chooses_var[1].upper(), 0, 0, True)
    signed_block_displayer()
    return final_result(sign_chooses_var[0].upper(), sign_chooses_var[1].upper())

while True:
    is_bot = None
    before_start()
    x_empty_list = [' ']*9
    x1,x2,x3,x4,x5,x6,x7,x8,x9 = tuple(x_empty_list)
    x_list = [x1,x2,x3,x4,x5,x6,x7,x8,x9]
    used_blocks = set()
    win_patterns = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    sign_chooses_var = sign_chooses()

    random_player_turn_true = None
    random_player_turn_false = None
    final_result_var = None

    print('Now, I will tell you who plays first.')
    print('Let me think...')
    random_player_turn = random.randint(1,2)
    if is_bot == True and random_player_turn == 1:
        print('You will play first!\n')
        random_player_turn_true = 1
    elif is_bot == True and random_player_turn == 2:
        print('Bot will play first!\n')
        random_player_turn_true = 2
    elif is_bot == False and random_player_turn == 1:
        print('Player 1 will play first!\n')
        random_player_turn_false = 1
    elif is_bot == False and random_player_turn == 2:
        print('Player 2 will play first!\n')
        random_player_turn_false = 2
    
    bot_playing_first = 0 
    while True:
        if random_player_turn_true == 1:
            final_result_var = combined_fun_p1()
            if final_result_var == True:
                break
            
            final_result_var = combined_fun_p2()
            if final_result_var == True:
                break

        elif random_player_turn_true == 2:
            bot_playing_first += 1
            final_result_var = combined_fun_p2()
            if final_result_var == True:
                break

            final_result_var = combined_fun_p1()
            if final_result_var == True:
                break

        elif random_player_turn_false == 1:    
            final_result_var = combined_fun_p1()
            if final_result_var == True:
                break
            
            final_result_var = combined_fun_p2()
            if final_result_var == True:
                break

        elif random_player_turn_false == 2:
            final_result_var = combined_fun_p2()
            if final_result_var == True:
                break

            final_result_var = combined_fun_p1()
            if final_result_var == True:
                break

    play_again_question = play_again()
    if play_again_question == False:
        break 
