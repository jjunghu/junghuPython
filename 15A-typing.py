# 타자게

import random
import time

def choice_animal():
    animal = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']
    ani = random.choice(animal)
    return ani

i = 1
input('타자게임을 시작할 준비가 되었으면 [Enter]를 눌러주세요.')
start = time.time()
q = choice_animal()
while i <= 5:
    print('*문제',i)
    print(q)
    type = input()

    if q == type:
        print('정확하게 타이핑하셨습니다')
        i = i +1
        q = choice_animal()
    else:
        print('오타입니다. 다시!')

end = time.time()
et = round(end - start, 2)
print('타자 문제를 모두 입력하는 데 걸린 시간은 %.2f초 입니다.' %et)
        

    
