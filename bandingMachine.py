# Banding Machine
print('[음료 자판기]')
print('1 : 콜라 (1200원) ')
print('2 : 사이다 (1000원) ')
print('3 : 물 (500원) ')
print('4 : 커피 (1500원) ')
option = input('음료를 골라주세요 (1-4) : ')
payment = int(input('돈을 넣어주세요 : '))
payback = payment
change = 0
### Select Menu and Pay
if payment >= 500:
    if option == '1':
        menu = '콜라'
        change =  payment - 1200
    elif option == '2':
        menu = '사이다'
        change = payment - 1000
    elif option == '3':
        menu = '물'
        change = payment - 500
    elif option == '4':
        menu = '커피'
        change = payment - 1500
    else:
        print('매뉴를 다시 선택하여 주세요 (1-4)')
else:print('금액이 부족합니다')
### If Change < 0, Withdraw the Money and Display instruction
if change < 0: 
    print('금액이 부족합니다. 다른 메뉴를 선택하세요')
else:
    print()
    print('[', menu, ']가 나왔습니다.')
    print('잔돈은 ',change, ' 원 입니다.')



