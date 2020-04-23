from django.contrib import admin
from .models import Review

# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('user', 'title', 'movie_title', 'rank', 'content')

# admin.site.register(Review, ReviewAdmin)
admin.site.register(Review)