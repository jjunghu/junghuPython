# 숫자 맞추

import random

n = random.randint(1, 50)

while True:
    x = input('맞혀보세요?')
    g = int(x)

    if g == n:
        print('정답입니다!! 추카추카')
        break
    else:
        if g > n:
            print('너무 커요!')
        else:
            print('너무 작아요!')
        
