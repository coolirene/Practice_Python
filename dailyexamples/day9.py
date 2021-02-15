# Day 9. Challenge 2- Leap Year Calculation
##
print('\n입력된 연도가 윤년인지 아닌지 판단하는 프로그램을 만들어보세요.')
# Repeat 3 times
for index in range(3):
    year = int(input('연도를 입력하시오 : '))  
    if year%4 == 0 & (year%100 != 0 | year%400 == 0):
        print('{0}년은 \033[93m윤년\033[0m입니다\n'.format(year))         
    else: print('{0}년은 윤년이 아닌 평년입니다. \n'.format(year))

    

      
    
