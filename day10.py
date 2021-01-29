# Day 10. Functions - To find whether the given number is an even or odd number

## function  to find Even/Odd 
def even_oddNum(num):
    if(num%2 != 0): print("홀수입니다!\n")
    else: print("짝수입니다!\n")

# main
print('\n정수를 한 개 입력받고, 해당 정수가 짝수인지 홀수인지 판단하는 함수를 만들어 보세요.')
num = int(input('정수를 입력하세요 : '))  
even_oddNum(num)
