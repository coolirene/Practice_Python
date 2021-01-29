# String Formatting
## Converting Hours and Minutes
print('[시간, 분 변환 프로그램]')
print('1 : 시간 ➡ 분')
print('2 : 분 ➡ 시간')
option = input('선택하세요(1 또는 2) : ')
time = int(input('시간을 입력하세요 : '))

if option == '1':
    convertM = time * 60
    print('시간을 분으로 환산했습니다.')
    print('{}분입니다.'.format(convertM))
elif option == '2':
    convertH = round(time/60)
    print('분을 시간으로 환산했습니다.')
    print('{}시간 입니다.'.format(convertH))
else: print('1 혹은 2를 입력하세요')