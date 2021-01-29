# Weekly Mission -  No 1. [난이도 "중"] 마름모 만들기

# Function to make a Rhomobus using *
def make_rhomobus(n):
    t = '*'
    x = ' '
    if(n%2 != 0): # n is odd, print starting from line 1
        for i in range(1, n+1, 2): # traingle -line spacing 2
            print(x * int((n-i)/2), t*i) # Space + print'*'
        for i in range(n-2, -1, -2): # reversed triangle
            print(x * int((n-i)/2), t*i) 
    else: # n is even, print starting from line 2
        for i in range(2, n+2, 2):
            print(x * int((n-i)/2), t*i)
        for i in range(n-2, -1, -2):
            print(x * int((n-i)/2), t*i)  

# main
while True:
    try:
        n = int(input('마름모를 만들기 위한 줄수를 입력하세요. 2 이상의 숫자를 입력하세요.  : '))
        if n >= 2: break
        else: print('2 이상의 수를 입력하세요.\n')
    except ValueError:
        print('2 이상의 정수만 입력하세요.')
print()
make_rhomobus(n)
    
    
