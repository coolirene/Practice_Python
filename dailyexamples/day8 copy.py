# Day 8. Challenge 1 - Print Grades

print('''
시험 점수를 입력받아
 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 
 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
* 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
''')



# grade = ''
# score = 0
# try:
#     score = int(input('점수를 입력하세요 (0 ~ 100) : '))
#     if score < 0 or score > 100: 
#         raise NotImplementedError
    
#     print('nnn')
#     print('\n잘못된 점수입니다. 점수를 다시 입력해 주세요. (0 ~ 100) \n')
# except NotImplementedError:
#     if 90 <= score <= 100: grade = 'A'
#     elif 80 <= score < 90: grade = 'B'
#     elif 70 <= score < 80: grade = 'C'
#     elif 60 <= score < 70: grade = 'D'
#     else: grade = 'F'   
#     print('\n당신의 학점은 {0}\n'.format(grade))

def printgrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 65:
        return "D"
    else:
        return "F"

def main():
    score = ''
    while score not in range(0,101):
        try:
            score = int(input("Enter a score: "))
        except ValueError:
            print('Invalid Entry')
    print("Your grade is:", printgrade(score))

main()
      
    
