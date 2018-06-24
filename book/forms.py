from django import forms

# 登录
class UserForm(forms.Form):
    typeItem = (
        ('user', "用户"),
        ('admin', "管理员"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    type = forms.ChoiceField(label="角色类型",choices=typeItem)

# 注册
class SignupForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    typeItem = (
        ('user', "用户"),
        ('admin', "管理员"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    type = forms.ChoiceField(label="角色类型", choices=typeItem)


# 修改密码
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label="旧密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(label="新密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password_confirm = forms.CharField(label="重输新密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# 添加图书
class AddFormBook(forms.Form):
    book_name = forms.CharField(label="图书名称", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    book_author = forms.CharField(label="图书作者", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    book_press = forms.CharField(label="出版社", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    book_num = forms.IntegerField(label="图书库存", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    book_sort = forms.CharField(label="图书分类", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    book_recore = forms.DateField(label="图书入库时间", widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    book_publish_date = forms.DateField(label="图书出版时间", widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))



