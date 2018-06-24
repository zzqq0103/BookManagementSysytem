from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

admin.site.register(User)
admin.site.register(Administrator)

# class MyUserInline(admin.StackedInline):
#     model = User
#     can_delete = False
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (MyUserInline,)
#
#
# admin.site.unregister(Admin, UserAdmin)
# admin.site.register(User, UserAdmin)
# admin.site.register(Book)