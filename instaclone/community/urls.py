from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='index'),
    path('<article_pk>/', views.detail, name='detail'),
    path('<article_pk>/comments_create', views.comments_create, name='comments_create'),
    path('<article_pk>/<comment_pk>/comments_delete', views.comments_delete, name='comments_delete'),

]