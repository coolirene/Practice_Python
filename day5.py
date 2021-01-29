# Day 5. Type Conversion on Input Value

# input Integer
var_a = int(input("a의 값(Integer) : "))
var_b = int(input("b 의 값(Integer) : "))
print('Input Value Type >>>> ', type(var_a),(type(var_b)))
print()
print('a + b = ', (var_a + var_b))
print('a - b = ', (var_a - var_b))
print('a * b = ', (var_a * var_b))
print('a / b = ', float(var_a / var_b))
print('a // b = ', (var_a // var_b))
print('a // b 의 나머지 = ', (var_a % var_b))
# input String
name, age, height =  input('\nEnter your Name, Age and Height by Space : ').split()
print('Input Value Type >>>> ', type(name), type(age), type(height))
print('Your Information : ', name, age, height)
print()