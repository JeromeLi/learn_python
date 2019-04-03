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


# define special character check function
def specical_char_check(x):
    security_str = r''''~!@#$%^&*()_=-/,.?<>;:[]{}|\'''
    for each in x:
        if each in security_str:
            return True
        else:
            return False



if pass_tmp.isdigit() or pass_tmp.isalpha() or len(pass_tmp) <= 8:
    print('Your password security level has been evaluate! Level => LOW ')
    print('Please raise your password security level!')
    print('Keep it up!')
elif pass_tmp.isalnum() or (pass_tmp.isdigit() and )
