# 문제 만들기 

import random

def make_question():
    a = random.randint(1, 40)
    b = random.randint(1, 20)
    op = random.randint(1, 3)

    q = str(a)

    if op == 1:
        q = q + '+' + str(b)
    if op == 2:
        q = q + '-' + str(b)
    if op == 3:
        q = q + '*' + str(b)

    return q

good = 0
bad = 0

for i in range(5):
    q = make_question()
    print(q)
    ans = int(input('='))

    if eval(q) == ans:
        print('정답입니다!')
        good = good + 1
    else:
        print('오답입니다ㅠㅠ')
        bad = bad + 1

print('당신의 정답갯수는 %d개 오답갯수는 %d개 입니다.' %(good, bad))

if bad == 0:
    print('당신은 천재군요!!')
