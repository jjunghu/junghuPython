# 타자게임2

import random
import time

sentence = ['우리 집 강아지 이름은 여름입니다', '이한이는 귀엽습니다', 'hello i am bottle', '일본어 쉽고 재미있게 가자'
            , '마구로 센세의 본격 일본어 이야기', '충청남도 아산 교육지원청 아산도서관', 'New 다이나믹 일본어'
            , '당신의 미래 etf 투자가 답이다', '너무너무 배가 고파요 집에 가고싶어요']

n = 1
input('타자게임을 시작하실 준비가 되었으면 [Enter]를 눌러주세요')
start = time.time()
q = random.choice(sentence)

while n <= 5:
    print('*문제', n)
    print(q)
    type = input()

    if q == type:
        print('통과!')
        n = n + 1
        q = random.choice(sentence)
    else:
        print('오답! 다시 입력하세요')

end = time.time()
et = end - start
print('당신의 타자시간은 %.2f초 입니다.' %et)
