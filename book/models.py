from __future__ import unicode_literals
from django.db import models

# Create your models here.

# 用户表 的模型设计（通过Django的 ORM 机制映射到 Mysql中的数据表的设计）
class User(models.Model):
    userid = models.AutoField(primary_key=True,verbose_name='用户编号')
    username = models.CharField(max_length=128,verbose_name='用户姓名')
    userpasswd = models.CharField(max_length=128,verbose_name='用户密码')
    usergender = models.CharField(max_length=32, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='性别')
    # user_phone = models.PhoneNumberField(verbose_name='用户电话号码')
    useremail = models.EmailField(verbose_name='用户邮箱',unique=True)
    permission = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username
    
    def __str__(self):
        return self.username


# 管理员表 的模型设计（通过Django的 ORM 机制映射到 Mysql中的数据表的设计）
class Administrator(models.Model):
    adminid = models.AutoField(primary_key=True)
    adminname = models.CharField(max_length=16,verbose_name='管理员姓名')
    adminpasswd = models.CharField(max_length=128,verbose_name='管理员密码')
    admingender = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='性别')
    # admin_phone = models.PhoneNumberField(verbose_name='管理员号码')
    adminemail = models.EmailField(verbose_name='管理员邮箱')
    permission = models.IntegerField(default=1)

    def __str__(self):
        return self.adminname

    def __unicode__(self):
        return self.adminname



# 图书表 的模型设计（通过Django的 ORM 机制映射到 Mysql中的数据表的设计）
class Book(models.Model):
    bookid = models.AutoField(primary_key=True,verbose_name='图书编号')
    bookname = models.CharField(max_length=128,verbose_name='图书名称')
    bookauthor = models.CharField(max_length=128,verbose_name='图书作者')
    bookpress = models.CharField(max_length=128,verbose_name='图书出版社')
    booknum = models.IntegerField(verbose_name='图书数量')
    booksort = models.CharField(max_length=128,verbose_name='图书类别')
    bookrecore = models.DateField(verbose_name='图书入库时间')
    bookpublishdate = models.DateField(verbose_name='图书出版时间')
    members = models.ManyToManyField(
        User,
        through='BookBorrow',  ## 自定义中间表
    )

    def __str__(self):
        return self.bookname

    def __unicode__(self):
        return self.bookname

    # 按照“book_name"属性名的顺序排列
    class META:
        ordering = ['bookname']


# 图书借书表 的模型设计（通过Django的 ORM 机制映射到 Mysql中的数据表的设计）
class BookBorrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowdate = models.DateField(verbose_name='借书时间')
    borrownum = models.IntegerField(default=0,verbose_name='借书数量')
    # return_date = models.DateField(verbose_name='还书时间')



