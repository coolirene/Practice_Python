# Day 7. FOR & WHILE LOOP
## For Loop
print('\n1. 1부터 100 까지의 수 중에서 3의 배수 이면서 \
    2의 배수는 아닌 수의 개수를 출력해 보세요.')
times3 = list() 
for i in range(1, 101): # range 1-100
    if(i%3 == 0 and i%2 != 0):
        times3.append(i)
print('결과값 : {0}'.format(times3))
print('결과값의 개수 : {0}'.format(len(times3)))
print()

## While Loop
print('4자리 비밀번호를 설정하고, 사용자로부터 그 비밀번호가 입력될 때까지\
 계속 비밀번호를 입력하도록 하는 프로그램을 만들어보세요')
while True:
    password = input('\n4자리 수의 비밀번호를 입력하세요. ')
    if password == '0909':
        print('맞았습니다!\n')
        break;
    else:
        print('틀렸습니다!\n')
    