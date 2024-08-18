# 가위바위보 게임1

import random

gbb_list = ['가위', '바위', '보']
win = 0
lose = 0
draw = 0
ans = 'YES'

while ans == 'YES':
    while True:
        player = input('가위 바위 보 중 하나를 선택하여 입력해주세요 : ')
        if player in gbb_list:
            print('당신의 선택은 %s입니다.' %player)
            break
        else:
            print('다시 입력해주세요')
            
    com = random.choice(gbb_list)
    print('컴퓨터의 선택은 %s입니다.' %com)

    if player == com:
        print('비겼습니다!')
        draw += 1
    elif (player == '가위' and com == '보') or (player == '바위' and com == '가위') or (player == '바위' and com == '가위'):
        print('플래이어 승!')
        win += 1
    else:
        print('컴퓨터 승!')
        lose += 1

    while True:
        ans = input('게임을 이어서 진행하시겠습니까? [YES / NO] : ')
        if ans.upper() in ['YES', 'NO']:
            break
        else:
            print('다시 정확히 입력해주세요 [YES / NO] : ')

print('당신의 승리는 %d회, 패배는 %d회, 무승부는 %d회 입니다!' %(win, lose, draw))
