import os
import random
def output_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

def imp_vars():
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,used_blocks,xls,win_patterns
    xt = [' ' for x in range(9)]
    x1,x2,x3,x4,x5,x6,x7,x8,x9 = tuple(xt)
    xls = [x1,x2,x3,x4,x5,x6,x7,x8,x9]
    used_blocks = set()
    win_patterns = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def before_start():
    global is_bot
    print('\nWelcome to the TicTacToe game!\n')
    while True:
        st = input('To play the game with Bot enter number 1, To play with your friend enter number 2\nIf you want to know about the game instructions enter help: ')
        output_cleaner()
        if st.lower() == '2':
            output_cleaner()
            is_bot = False
            print('game stated!\n')
            break
        elif st.lower() == '1':
            output_cleaner()
            print('game stated!\n')
            is_bot = True
            break
        elif st.lower() == 'help':
            output_cleaner()
            print('when the game starts you should enter one of these numbers so you can get that block with your sign\n')
            print('1','|','2','|','3')
            print('---------')
            print('4','|','5','|','6')
            print('---------')
            print('7','|','8','|','9\n')
            print('Player 1 sign\'s is X and Player 2 sign\'s is O\n')
        else:
            output_cleaner()
            print('Wrong input! try again')

def player_turn(player, sign, ib = False):
    if sign == 'X':
        n = 1
    elif sign == 'O' and ib == False:
        n = 2
    elif sign == 'O' and ib == True:
        n = 3
    

    while True:
        if is_bot == True:
            if n == 1:
                while True:
                    player = input(f'Which block you want to sign? ')
                    if player.isdigit() and 1<=int(player)<=9 :
                        player = int(player)
                        break
                    else:
                        output_cleaner()
                        print('You did not entered an integer number between 1-9! try again\n')
                        signed_block_displayer()
            else:
                player = random.randint(1,9)
        else:
            if n != 3:
                while True:
                    player = input(f'Player {n} which block you want to sign? ')
                    if player.isdigit() and 1<=int(player)<=9:
                        player = int(player)
                        break
                    else:
                        output_cleaner()
                        print('You did not entered an integer number between 1-9! try again\n')
                        signed_block_displayer()
        output_cleaner()
        if player not in used_blocks:
            used_blocks.add(player)
            xls[player-1] = sign
            break
        else:
            output_cleaner()
            print(f'The block that you choosed is Full!\n')
            signed_block_displayer()
    return True

def signed_block_displayer():
    print(f'{xls[0]} | {xls[1]} | {xls[2]}')
    print('---------')
    print(f'{xls[3]} | {xls[4]} | {xls[5]}')
    print('---------')
    print(f'{xls[6]} | {xls[7]} | {xls[8]}\n')

def final_result():
    for sign in ['X','O']:
        for a,b,c in win_patterns:
            if xls[a-1] == xls[b-1] == xls[c-1] == sign:
                output_cleaner()
                print('Game ended!\n')
                signed_block_displayer()
                if is_bot == True:
                    print('You won! :)' if sign == 'X' else 'You lost! :(')
                else:
                    if sign == 'X':
                        print('Player 1 You won ;)')
                        print('Player 2 you Lost :(')
                    else:
                        print('Player 2 You won ;)')
                        print('Player 1 you Lost :(')
                return True
    if all(x != ' ' for x in xls):
        output_cleaner()
        print('Game ended and result is Tie!\n')
        signed_block_displayer()
        return True

def play_again():
    while True:
        pa = input('\nDo you want to play again? Enter Yes or No: ').lower()
        output_cleaner()
        if pa == 'yes':
            return True
        elif pa == 'no':
            return False
        else:
            print('You did not entered yes or no! try again!')
        

while True:
    before_start()
    imp_vars()
    while True:
        player1 = None    
        player_turn(player1, 'X')
        signed_block_displayer()
        fr = final_result()
        if fr == True:
            break
        
        player2 = None
        if is_bot == False:
            player_turn(player2, 'O')
        elif is_bot == True:
            player_turn(player2, 'O', True)
        signed_block_displayer()
        fr = final_result()
        if fr == True:
            break
        
    play_again_question = play_again()
    if play_again_question == False:
        break 

    
