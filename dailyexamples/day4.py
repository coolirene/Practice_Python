# Day 4. Basic Operators
# A. Basic Operation
print("\n1) 두 수 a와 b를 선언한 뒤, a와 b를 이용한 사칙연산 계산기를 만들어 보세요.\n")
var_a = 5
var_b = 3

#1. Addition
print ("a + b = ", (var_a + var_b))
#2. Subtraction
print ("a - b = ", (var_a - var_b))
#3. Multiplication
print ("a * b = ", (var_a * var_b))
#4. Division
print ("a / b = ", (var_a / var_b))
#5. Floor Division
print ("a // b = ", (var_a // var_b))
#6. Modulus
print ("a // b 의 나머지 = ", (var_a % var_b))

# B. Exponent Calculation
print("\n2) 두 수 a와 b를 선언한 뒤, a의 b제곱의 값을 출력해보세요.")
intA = 3
intB = 4
# 1. Using Operator **
print ("a 의 b 제곱 = ", (intA ** intB))
# 2. Using function pow()
print ("a 의 b 제곱 = ", (pow(intA, intB)))