#계산기 만들기

def plus(num1, num2):
    print('%d + %d = %d' %(num1, num2, num1+num2))

def minus(num1, num2):
    print('%d - %d = %d' %(num1, num2, num1-num2))

def multiply(num1, num2):
    print('%d * %d = %d' %(num1, num2, num1*num2))

def divide(num1, num2):
    if num2 == 0:
        print('0으로 나눌 수 없습니다.')
    else:
        print('%d / %d = %.2f' %(num1, num2, num1/num2))

while True:
    print('수행할 사칙연산을 선택해주세요')
    print('1 : 덧셈')
    print('2 : 뺄셈')
    print('3 : 곱셈')
    print('4 : 나눗셈')
    method = int(input('1, 2, 3, 4 숫자 입력 : '))
    if method not in [1, 2, 3, 4]:
        print('정확하게 다시 입력해주세요')
        continue
    else:
        num1 = int(input('연산할 첫 번째 수를 입력해주세요 : '))
        num2 = int(input('연산할 두 번째 수를 입력해주세요 : '))
        if method == 1:
            plus(num1, num2)
        elif method == 2:
            minus(num1, num2)
        elif method == 3:
            multiply(num1, num2)
        else:
            print('소숫점 둘째자리에서 반올림하여 출력됩니다')
            divide(num1, num2)
        break
            
