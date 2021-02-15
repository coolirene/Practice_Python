# Day 8. Challenge 1 - Print Grades (Using While & If)

print('''
시험 점수를 입력받아
 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 
 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
* 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
''')
## variable init
grade = ''
score = -1

while score not in range(0, 101):
    try:
        score = int(input('점수를 입력하세요 (0 ~ 100) : '))
    except ValueError:
        print('\n잘못된 점수입니다. 점수를 다시 입력해 주세요. (0 ~ 100) \n')
    
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
print('\n당신의 학점은 {0} 입니다\n'.format(grade))


      
    
