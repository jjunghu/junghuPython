# 구구단 출력기

def gugudan(n):
    for i in range(1, 10):
        print('%d * %d = %d' %(n, i, n*i))

while True:
    num = int(input('2부터 9까지의 수를 입력하시면 구구단을 출력해드릴게요 : '))
    if num in [2, 3, 4, 5, 6, 7, 8, 9]:
        print(num, '단')
        gugudan(num)
        break
    else:
        print('다시 입력해주세요')
