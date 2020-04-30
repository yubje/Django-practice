from django.contrib import admin
from .models import Review, Comment

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'movie_title', 'rank', 'content')

class CommentAdmin(admin.ModelAdmin):
    list_diplay = ('user', 'content')

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)