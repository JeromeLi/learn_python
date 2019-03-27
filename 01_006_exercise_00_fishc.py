n = 0
line_num = 0
while n <= 100:
    if n % 2 != 0:
       print(n, end=' ')
       line_num += 1
       if line_num % 10 == 0:
           print('\n')
    n += 1


