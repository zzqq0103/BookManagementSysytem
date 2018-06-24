"""BookManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from book import views as book_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', book_views.index),
    url(r'^login/', book_views.login),
    url(r'^signup/', book_views.signup),
    url(r'^logout/', book_views.logout),
    url(r'^borrowed_list/', book_views.borrowed_list),
    url(r'^delete_book/', book_views.delete_book),
    url(r'^view_book_list/', book_views.view_book_list),
    url(r'^rent_book/', book_views.rent_book),
    url(r'^change_passwd/', book_views.change_passwd),
    url(r'^add_book/', book_views.add_book),
    url(r'^borrow/', book_views.borrow),
    url(r'^edit_book', book_views.edit_book)
]
