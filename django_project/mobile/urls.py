from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home,name='mobile-home'),
    path('index/', views.home,name='mobile-home'),
    path('about/', views.about,name='mobile-about'),
    path('viewall/', views.viewall,name='mobile-viewall'),
    path('action_show_page/', views.action_show_page, name='action-show-page')

]
