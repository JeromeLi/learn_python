member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
print('Original member:', member)
# member.append(88)
score = [88, 90, 85, 90, 88]
i = 0

for index_member in range(1, (len(member) + len(score)), 2):
    member.insert(index_member, score[i])
    i += 1
print('Modified member:', member)

# Output style 0
print('\n' + 'Output style 0:')
for k in member:
    print(k)

# Output style 1, Method 0
print('\n' + 'Output style 1:')
for n in range(0, len(member), 2):
    print(member[n], member[n + 1])

# Output style 1, Method 1
for p in range(len(member)):
    if p % 2 == 0:
        print(member[p], member[p + 1])
