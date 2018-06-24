# 判断是否已经登录（管理员或者是用户）

def ifLogon(user):
    if user.is_authenticated():
        return True
    else:
        return False