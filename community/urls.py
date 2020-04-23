from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('create/', views.create, name='create'),
    path('<review_pk>/', views.review_detail, name='review_detail'),
    path('<review_pk>/update', views.update, name='update'),
    path('<review_pk>/delete', views.delete, name='delete'),
]