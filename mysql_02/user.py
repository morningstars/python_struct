from login import Login

user = Login()
while True:
    style = input("login or register:")

    if style == 'register':
        username = input("username:")
        password = input("password:")
        if user.register(username, password):
            print("注册成功")
        else:
            print("注册失败")
    elif style == 'login':
        username = input("username:")
        password = input("password:")

        if user.login(username, password):
            print("登录成功")
        else:
            print("登录失败")
    else:
        print('wrong input')
