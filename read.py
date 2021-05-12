# 讀取資料並存入清單list
'''
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了， 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
print('平均是', sum_len / len(data))
'''

# 對清單list的篩選
'''
data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
'''

# 對清單list的指定文字內容之篩選
'''
data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言包含 good')
print(good[10])
'''

# list comprehension-->清單快寫法
'''
data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆留言包含 good')
print(good[100])
'''

# list comprehension-->清單快寫法-->進階用法
'''
data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
good = ['bad' in d for d in data]
print(good[101])
'''

# range 範圍-->清單產生器
'''
90%以上，我們寫這種for i in range()的for loop只是為了讓它的內容重複執行某個"固定次數"
# 10是結尾值，不包含在內
import random
for i in range(100):
    r = random.randint(1, 6)
    print('這是第', i + 1, '次產生隨機數： ', r)
'''

# range 範圍-->清單產生器-->延伸
'''
data = range(2, 10, 3)
print(data)
for i in data:
    print(i)

data1 = list(range(2, 10, 3))
data2 = list(range(10, 3, -2))
print(data1, data2)
'''
