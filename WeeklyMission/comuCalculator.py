# Weekly Mission -  No 2. [난이도 "상"] 계산기 만들기

import random as rd

# Addition - 4 numbers
numbers = range(1, 11) # Only Operate on 1 digit numbers
add_list = rd.sample(numbers, 4)
# print(add_list)
last = add_list.pop(-1) # Coz no operator for ths last number

for i in add_list:
    print(i,end='+') # Print elements with '+'
# append the last element
print(last)
# Adding all elements
print (sum(add_list) + last)
print()

# Subtraction and Adding combination - 6 numbers
minus = 0
plus = 0
subt_list = rd.sample(numbers, 6)

# print(subt_list)
last = subt_list.pop(-1)  # Coz no operator for ths last number

# Used + and shift based on the index number
for i, val in enumerate(subt_list):
    if i%2 == 0:
        print(val,end='-')
        plus += val
    else: 
        print(val,end='+')
        minus += val
print(last)
print()
print(plus - minus - last)       