count_max = 3
password = 'FishC.com'
while count_max:
    input_str = input('Please input password:')
    if '*' in input_str:
        print('password have a "*"! you have', count_max, 'chances!', end='')
    elif input_str == password:
        print('Password is correct, enter progress......')
        break
    else:
        count_max -= 1
        print('Password is incorrect! you have', count_max, 'chances!')
        continue
