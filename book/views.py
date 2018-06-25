from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from . import models
from . import forms
from itertools import chain

# 主页
def index(request):
    pass
    return render(request, 'book/index.html')



# 登录
def login(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            type = login_form.cleaned_data['type']
            print('type:'+type)
            try:
               if type == 'user':
                   user = models.User.objects.get(username=username)
                   if user.userpasswd == password:
                       request.session['is_login'] = True
                       request.session['user_id'] = user.userid
                       request.session['user_name'] = user.username
                       request.session['permission'] = user.permission
                       request.session['password'] = user.userpasswd
                       return redirect('/index/')
                   else:
                       message = "密码不正确！"
               else:
                   admin = models.Administrator.objects.get(adminname=username)
                   if admin.adminpasswd == password:
                       request.session['is_login'] = True
                       request.session['user_id'] = admin.adminid
                       request.session['user_name'] = admin.adminname
                       request.session['permission'] = admin.permission
                       request.session['password'] = admin.adminpasswd
                       return redirect('/index/')
                   else:
                       message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'book/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'book/login.html', locals())


# 注销
def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")

# 注册
def signup(request):
    if request.method == "POST":
        register_form = forms.SignupForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            type = register_form.cleaned_data['type']
            if type == 'user':
                if password1 != password2:  # 判断两次密码是否相同
                    message = "两次输入的密码不同！"
                    return render(request, 'book/signup.html', locals())
                else:
                    same_name_user = models.User.objects.filter(username=username)
                    if same_name_user:  # 用户名唯一
                        message = '用户已经存在，请重新选择用户名！'
                        return render(request, 'book/signup.html', locals())
                    same_email_user = models.User.objects.filter(useremail=email)
                    if same_email_user:  # 邮箱地址唯一
                        message = '该邮箱地址已被注册，请使用别的邮箱！'
                        return render(request, 'book/signup.html', locals())
                    # 当一切都OK的情况下，创建新用户
                    new_user = models.User()
                    new_user.username = username
                    new_user.userpasswd = password1
                    new_user.useremail = email
                    new_user.usergender = sex
                    new_user.permission = 0
                    new_user.save()
                    return redirect('/login/')  # 自动跳转到登录页面
            else:
                if password1 != password2:  # 判断两次密码是否相同
                    message = "两次输入的密码不同！"
                    return render(request, 'book/signup.html', locals())
                else:
                    same_name_user = models.Administrator.objects.filter(adminname=username)
                    if same_name_user:  # 用户名唯一
                        message = '用户已经存在，请重新选择用户名！'
                        return render(request, 'book/signup.html', locals())
                    same_email_user = models.Administrator.objects.filter(adminemail=email)
                    if same_email_user:  # 邮箱地址唯一
                        message = '该邮箱地址已被注册，请使用别的邮箱！'
                        return render(request, 'book/signup.html', locals())
                    # 当一切都OK的情况下，创建新用户
                    new_user = models.Administrator()
                    new_user.adminname = username
                    new_user.adminpasswd = password1
                    new_user.adminemail = email
                    new_user.admingender = sex
                    new_user.permission = 1
                    new_user.save()
                    return redirect('/login/')  # 自动跳转到登录页面

    register_form = forms.SignupForm()
    return render(request, 'book/signup.html', locals())

# 设定密码
def change_passwd(request):
    if request.method == "POST":
        change_password_form = forms.ChangePasswordForm(request.POST)
        message = "请检查填写的内容！"
        if change_password_form.is_valid():  # 获取数据
            password_old = change_password_form.cleaned_data['old_password']
            password_new = change_password_form.cleaned_data['new_password']
            password_new_confirm = change_password_form.cleaned_data['new_password_confirm']
            print(password_old+' '+password_new+ ' '+password_new_confirm)
            if password_new_confirm != password_new:  # 判断两次密码是否相同
                message = "两次输入的新密码不同！"
                return render(request, 'book/set_password.html', locals())
            else:
                username = request.session.get('user_name')
                print('username'+ username)
                if request.session.get('permission'):
                    # 更新管理员 用户密码
                    admin = models.Administrator.objects.filter(adminname=username)
                    if admin:
                        passwd = models.Administrator.objects.filter(adminname=username, adminpasswd=password_old)
                        if passwd:
                            models.Administrator.objects.filter(adminname=username, adminpasswd =password_old).update(adminpasswd=password_new);
                            print('admin_correct')
                            message = '密码修改成功！'
                        else:
                            message = '请检查旧密码是否输入正确!'
                    return redirect('/index/')  # 自动跳转到登录页面
                else:
                    # 更新用户 用户密码
                    user = models.User.objects.filter(username=username)
                    if user:
                        passwd = models.User.objects.filter(username=username, userpasswd=password_old)
                        if passwd:
                            models.User.objects.filter(username=username, userpasswd=password_old).update(userpasswd=password_new);
                            print('user_correct')
                            message = '密码修改成功！'
                        else:
                            message = '请检查旧密码是否输入正确!'

                    return redirect('/index/')  # 自动跳转到登录页面

    change_password_form = forms.ChangePasswordForm()
    return render(request, 'book/set_password.html', locals())


# 查看图书 (无需登录即可查看）
def view_book_list(request):
    category_list = models.Book.objects.values_list('bookname', flat=True).distinct()
    query_category = request.GET.get('book_name', 'all')
    if (not query_category) or models.Book.objects.filter(bookname=query_category).count() is 0:
        query_category = 'all'
        book_list = models.Book.objects.all()
    else:
        book_list = models.Book.objects.filter(bookname=query_category)

    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        book_list = models.Book.objects.filter(bookname=keyword)
        query_category = 'all'

    paginator = Paginator(book_list, 5)
    page = request.GET.get('page')
    try:
        book_list = paginator.page(page)
    except PageNotAnInteger:
        book_list = paginator.page(1)
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)
    content = {
        'category_list': category_list,
        'query_category': query_category,
        'book_list': book_list,
    }
    return render(request, 'book/view_book_list.html', content)


# -------------------------------------------------------用户---------------------------------------------------------

# 查看已借阅图书列表 （用户）
def borrowed_list(request):
    if request.session.get('is_login'):
        borrower_id = request.session.get('user_id')
        print('borrower_id:')
        print(borrower_id)
        borrowbook_list = models.BookBorrow.objects.filter(user__userid=borrower_id)
        count = borrowbook_list.count()
        content = {
            "borrow_book_list": []
        }
        if count:
            sumlist = []
            while count:
                print("borrowbook_list:")
                print(borrowbook_list)
                user_list = models.User.objects.filter(bookborrow__user__userid=borrower_id)
                print('user_list:')
                print(user_list)
                book_list = models.Book.objects.filter(bookborrow__user__userid=borrower_id)
                print('book_list:')
                print(book_list)
                list_clone = list(chain(user_list, borrowbook_list, book_list))
                print(list_clone)
                for book in list_clone:
                    print(book)
                sumlist.append(list_clone)
                count = count - 1
            content = {
                "borrow_book_list": sumlist
            }
            for book in sumlist:
                print(book[0].userid)
            return render(request, 'book/borrow_book.html', content)
        return render(request, 'book/borrow_book.html', content)




# 借书操作（用户）
def borrow(request):
    pass


# 归还图书操作 （用户）
def rent_book(request):
    pass


 # ------------------------------------------------------- 管理员 ------------------------------------------

# 添加图书 （管理员权限）

def add_book(request):
    if request.session.get('permission'):
        add_book_form = forms.AddFormBook(request.POST)
        message = "请检查填写的内容！"
        if add_book_form.is_valid():  # 获取数据
            book_name = add_book_form.cleaned_data['bookname']
            book_author = add_book_form.cleaned_data['bookauthor']
            book_press = add_book_form.cleaned_data['bookpress']
            book_num = add_book_form.cleaned_data['booknum']
            book_sort = add_book_form.cleaned_data['booksort']
            book_recore = add_book_form.cleaned_data['bookrecore']
            book_publish_date = add_book_form.cleaned_data['bookpublish_date']
            same_book = models.Book.objects.filter(book_name=book_name)
            if same_book:
                same_book.book_num += book_num
                same_book.save()
            else:
                newBook = models.Book()
                newBook.bookname = book_name
                newBook.bookauthor = book_author
                newBook.bookpress = book_press
                newBook.booknum = book_num
                newBook.bookrecore = book_recore
                newBook.bookpublishdate = book_publish_date
                newBook.save()
            return redirect('/index/')  # 自动跳转到登录页面
        add_book_form = forms.AddFormBook()
    return render(request, 'book/add_book.html', locals())


# 删除图书 （管理员权限）

def delete_book(request):
    bookid = request.GET.get('bookid')
    if bookid:
        print('bookid' + bookid)
        delete_item = models.Book.objects.get(pk=bookid)
        if delete_item:
            models.Book.objects.get(pk=bookid).delete() # 级联删除数据
            redirect("/delete_book/")

    book_list = models.Book.objects.all()
    count = book_list.count()
    if not count:
        book_list = {}
    content = {
        'book_list': book_list,
    }
    return render(request, 'book/delete_book.html', content)


# 修改图书信息(管理员权限）

def edit_book(request):
    if request.session.get('permission'):
        category_list = models.Book.objects.values_list('bookname', flat=True).distinct()
        query_category = request.GET.get('book_name', 'all')
        if (not query_category) or models.Book.objects.filter(bookname=query_category).count() is 0:
            query_category = 'all'
            book_list = models.Book.objects.all()
        else:
            book_list = models.Book.objects.filter(bookname=query_category)

        if request.method == 'POST':
            keyword = request.POST.get('keyword', '')
            book_list = models.Book.objects.filter(bookname=keyword)
            query_category = 'all'

        paginator = Paginator(book_list, 5)
        page = request.GET.get('page')
        try:
            book_list = paginator.page(page)
        except PageNotAnInteger:
            book_list = paginator.page(1)
        except EmptyPage:
            book_list = paginator.page(paginator.num_pages)
        content = {
            'category_list': category_list,
            'query_category': query_category,
            'book_list': book_list,
        }
        return render(request, 'book/edit_book.html', content)
    else:
        return redirect("/index/")


# 删除用户（管理员权限）

def deleteUser(request):
    userid = request.GET.get('userid')
    if userid:
        print('userid' + userid)
        delete_item = models.User.objects.get(pk=userid)
        if delete_item:
            models.User.objects.get(pk=userid).delete() // 级联删除数据
            redirect("/user_list/")

    user_list = models.User.objects.all()
    count = user_list.count()
    if not count:
        book_list = {}
    paginator = Paginator(user_list, 5)
    page = request.GET.get('page')
    try:
        user_list = paginator.page(page)
    except PageNotAnInteger:
        user_list = paginator.page(1)
    except EmptyPage:
        user_list = paginator.page(paginator.num_pages)
    content = {
        'user_list': user_list,
    }
    return render(request, 'book/user_list.html', content)



# 查看已注册用户列表（管理员权限）
def view_User_List(request):
    pass

