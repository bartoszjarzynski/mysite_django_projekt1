from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('post/<int:post_id>/', views.post_page, name='post_page'),
    path('add_post/', views.add_post, name='add_post'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
]
