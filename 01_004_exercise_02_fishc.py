temp_int = input('Please input a positive integer number:')
print (isinstance(temp_int, int))
loop_num = int(temp_int)
while loop_num:
    print(' ' * (loop_num - 1) + '*' * loop_num)
    loop_num = loop_num - 1
