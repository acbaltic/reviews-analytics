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
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
'''

