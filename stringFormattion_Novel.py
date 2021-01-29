# String Formatting - Write Novel
print ('')
title = input('이 소설의 제목: ') # 명란젓
verb1 = input('동사1: ') # 먹는다
verb2 = input('동사2: ') # 뛰어
noun1 = input('명사1: ') # 밥
noun2 = input('명사2: ') # 초밥
noun3 = input('명사3: ') # 병원
noun4 = input('명사4: ') # 기린
noun5 = input('명사5: ') # 코끼리
noun6 = input('명사6: ') # 커피
noun7 = input('명사7: ') # 대학원
adj1 = input('형용사1: ') # 눈이 부셔
adj2 = input('형용사2: ') # 멋지다

print()
print(f'------제목: {title}------')
print(f'시동이 걸리지 않았다. 브레이크를 밟은 상태에서 버튼을 눌러야 한다고 그녀가\n')
print('가르쳐주었고 나는 그제야 제대로 시동을 걸 수 있었다.')
print(f'\33[32m"자, {verb1}"\033[0m')
print(f'브레이크에서 떼어낸 {noun1}으로 옮겨 밟았다. 차가 움직이기 시작했다.')
print(f'\33[32m"어허, 그렇게 콱콱 밟지 말고 {adj1} 눌러야지. 그치, 그렇게."\033[0m')
print(f'근데 왜 반말을 하지, 라고 생각하고 있는데 그녀가 {noun2}을 조정하면서 날카롭게 말했다.')
print(f'\33[32m"{noun3}이 좀 짧을 수 있어요."\033[0m')
print(f'도로연수를 하다보면 {noun4}이 없으니까 \33[32m"요"\033[0m자를 붙일 시간이 없다는 것이었다.')
print(f'{noun5}을 위한 것이라고 하니 탐탁지는 않지만 수긍할 수밖에 없었다.')
print(f'내가 {adj2} 네. 라고 대답하자 그녀가 처음으로 입가에 옅은 미소를 띠면서 {verb2}.')
print(f'\33[32m"내 눈에 초보들은 다 {noun6} 같단 말이야."\033[0m')
print('그리고 덧붙였다.')
print(f'\33[32m"그것도 갓 태어난 {noun7}."\033[0m')
