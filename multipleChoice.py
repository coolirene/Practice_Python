# Multiple Choice - using Conditions
## Question 1
print('1. 다음 중 옳은 것을 하나만 고르시오. (5점)')
print('파이썬의 자료형에는______이 있다.')
print('1)친척형 2)아는형 3)우리형 4)실수형 5)변수형')
print()

score = 0
ans = input('1번 답의 번호를 적어주세요: ')
if ans == '4': score +=5
else: score += 0
print()
## Question 2
print('1. 다음 중 옳은 것을 하나만 고르시오. (5점)')
print('파이썬의 형변환에는 ______가 있다.')
print('1)float() 2)stl() 3)florida() 4)ins() 5)sto()')

ans = input('2번 답의 번호를 적어주세요: ')

if ans == '1': score +=5
else: score += 0

print('\n-----채점 결과-----')
print('총점은 {} 점입니다.'.format(score))