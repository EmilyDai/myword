from django.contrib import admin
 
from .models import Column, Word,Function,User,Comment
 
class FunctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro','nav_display', 'home_display')
    
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro')
 
 
class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content',)
 
admin.site.register(Function, FunctionAdmin) 
admin.site.register(Column, ColumnAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)