#가위바위보 게임2
import random

rsp = ['rock', 'scissors', 'paper']
wins = 0
loses = 0
draws = 0
restart = 'y'

while restart == 'y':
    player_rsp = input('Rock / Scissors / Paper 중 하나를 선택하여 입력해주세요 : ')
    player = player_rsp.lower()
    if player not in rsp:
        print('please type correctly')
        continue
    else:
        print('You: ' , player)

    com = random.choice(rsp)
    print('Computer: ' , com)

    if player == com:
        print('Draws!')
        draws += 1
    elif (player == 'rock' and com == 'scissors') or (player == 'scissors' and com == 'paper') or (player == 'paper' and com == 'rock'):
        print('You Win!')
        wins += 1
    else:
        print('You Lose!')
        loses += 1

    while True:
        restart1 = input('restart? [y / n] : ')
        restart = restart1.lower()
        if restart not in ['y', 'n']:
            print('please type correctly')
            continue
        elif restart == 'y':
            break
        else:
            print('%d승 %d패 %d무' %(wins, loses, draws))
            break
        
        
