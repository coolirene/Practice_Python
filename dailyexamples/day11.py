#Day 11. Lists - To find Sum Of Elements in List
## Take 7 integers by User
list = []
print('7개의 정수를 입력해 주세요.\n')
list = []
for i in range(7):
       elements = int(input())
       list.append(elements)
# print(list)
total = sum(list)
print("합계 : ", total)

