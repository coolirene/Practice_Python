# Day 6. Conditions & IF Statements

# 1. 세 개의 숫자를 입력 받은 후에, 그 세 개의 숫자 중에서 가장 큰 수를 출력하는 프로그램을 작성하세요.
## input 3 Numbers by User 
try:
    num1 = float(input("Enter the First Number : "))
    num2 = float(input("Enter the Second Number : "))
    num3 = float(input("Enter the Third Number : "))
except ValueError:
    print("\nPLZ Enter \033[91m Numbers\033[0m !!!\n")

### 1-1. By Number Cpmparison
if num1 >= num2 and num1 >= num3: 
    print("\n가장 큰 수는 \33[91m", num1, "\033[0m 입니다." )
elif num2 >= num1 and num2 > num3:
    print("\n가장 큰 수는 \33[91m", num2, "\033[0m 입니다." )
else:
    print("\n가장 큰 수는 \33[91m", num3, "\033[0m 입니다." )

### 1-2. By Max Function
print("\nMax를 사용한 가장 큰 수는 \33[91m", max(num1, num2, num3), "\033[0m 입니다." )

# 2. 한 문자열을 입력 받은 후에, 그 문자열 안에 "모각코"라는 단어가 들어있으면 "모각코! 좋아요!"를 
#    없으면 "모각코! 없어요ㅠ" 를 출력해주세요

### Input Strings by User >>> Try 3 times
n = 3
while n > 0:
    str = input("\nEnter Today's String : ")
    if "모각코" in str:
            print("\n모각코! 좋아요")
    else: 
            print("\n모각코! 없어요ㅠ")
    n -= 1
# Print a Message to be finished
print("\033[94m\nThanks! Bye Now ~~\033[0m\n")

