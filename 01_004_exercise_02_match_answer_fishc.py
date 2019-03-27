temp_int = input('Please input a positive integer number:')
loop_num = int(temp_int)

while loop_num:
    space_loop = loop_num - 1
    while space_loop:
        print(' ', end='')
        space_loop = space_loop - 1

    star_loop = loop_num
    while star_loop:
        print('*', end='')
        star_loop = star_loop - 1
    print()
    loop_num = loop_num - 1
8
