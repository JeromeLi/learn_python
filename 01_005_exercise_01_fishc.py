while True:
    input_year = input('Input year number:')
    if input_year.isdigit():
        break
    else:
        print('Please input a positive integer number!')
int_year = int(input_year)
if (isinstance(int_year / 4, int) and not isinstance(int_year / 100, int)) \
   or isinstance(int_year / 400, int):
    print('It\'s a leap year!')
else:
    print('It\'s not a leap year!')


