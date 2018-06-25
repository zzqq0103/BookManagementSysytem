from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^borrowed_list/', views.borrowed_list, name='borrowed_list'),
    url(r'^borrow/', views.borrow, name='borrow'),
    url(r'^delete_book/', views.delete_book, name='delete_book'),
    url(r'^view_book_list/', views.view_book_list, name='view_book_list'),
    url(r'^rent_book/', views.rent_book, name='rent_book'),
    url(r'^change_passwd/', views.change_passwd, name='change_passwd'),
    url(r'^add_book/', views.add_book, name='add_book'),
    url(r'^edit_book/', views.edit_book, name='edit_book'),
    url(r'^user_list/', views.deleteUser, name='user_list')
]