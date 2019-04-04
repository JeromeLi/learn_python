# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位


pass_tmp = input('Please enter the password you need to check:')

while (pass_tmp.isspace or len(pass_tmp)) == 0:
    pass_tmp = input('Please enter the password again!')


# define special character check function
def special_char_check(x):
    special_char = r'~!@#$%^&*()_=-/,.?<>;:[]{}|\''
    # print(special_char)
    for each in x:
        if each in special_char:
            return True
            break
    else:
        return False


def digital_char_check(x):
    digital_char = '1234567890'
    for each in x:
        if each in digital_char:
            return True
            break
    else:
        return False


def alpha_char_check(x):
    alpha_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for each in x:
        if each in alpha_char:
            return True
            break
    else:
        return False


if digital_char_check(pass_tmp) and alpha_char_check(pass_tmp) and special_char_check(pass_tmp) \
        and pass_tmp[0].isalpha() and len(pass_tmp) >= 16:
    print('Your password security level has been evaluate! Level => High ')
    print('Keep it up!')

elif ((digital_char_check(pass_tmp) and alpha_char_check(pass_tmp)) or \
      (digital_char_check(pass_tmp) and special_char_check(pass_tmp)) or \
      (alpha_char_check(pass_tmp) and special_char_check(pass_tmp))) and \
        len(pass_tmp) > 8:
    print('Your password security level has been evaluate! Level => Medium ')
    print('Keep it up!')

elif pass_tmp.isdigit() or pass_tmp.isalpha() or len(pass_tmp) <= 8:
    print('Your password security level has been evaluate! Level => LOW ')
    print('Please raise your password security level!')
