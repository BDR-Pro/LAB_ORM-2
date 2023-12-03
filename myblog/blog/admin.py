from django.contrib import admin

from .models import Post , Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image' ,  'published_at', 'category')
    list_filter = ('published_at', 'category')
    search_fields = ['title', 'content']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content' ,'created_at')
    list_filter = ('created_at','post')
    search_fields = ['user', 'content']


admin.site.register(Post , PostAdmin)
admin.site.register(Comment, CommentAdmin)
