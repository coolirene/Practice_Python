#사전 데이터 불러오기
import csv

f = open('kr-kor-word2.csv', 'r', encoding='utf-8-sig')
reader = csv.reader(f)
start_words = [] #첫글자
for line in reader:
    start_words.append(line)
f.close()

f = open('kr-kor-data-word.csv', 'r', encoding='utf-8-sig')
reader = csv.reader(f)
result = [] #단어
for line in reader:
    result.append(line)
f.close()

def get_words(start):
    text_list = []
    for i in result:
        #첫글자로 시작하는걸 추출
        if str(i).startswith(start):
            print(str(i))
            text_list.append(str(i))
    return text_list

attack_word_list = [] #끝글자로 시작하는 단어가 없는 단어
for word in start_words:
    if len(get_words(str(word))) == 0:
        for i in result:
            if str(i).endswith(str(word)):
                print(str(i))
                attack_word_list.append(str(i))

attack_word_list = list(set(attack_word_list))

f = open('kr-attack3.csv', 'w', encoding='utf-8-sig')
for i in attack_word_list:
    f.write(str(i)+'\n')
f.close()