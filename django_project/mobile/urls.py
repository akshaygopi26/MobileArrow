from django.urls import path
from . import views 
from  .views import (
    Viewall,
    MobileDetailView
)

urlpatterns = [
    path('', views.home,name='mobile-home'),
    path('index/', views.home,name='mobile-home'),
    path('about/', views.about,name='mobile-about'),
    path('viewall/',Viewall.as_view(),name='mobile-viewall'),
    path('mobile/<int:pk>',MobileDetailView.as_view(),name='mobile-detail'), 
    path('action_show_page/', views.action_show_page, name='action-show-page'),
    path('compare/', views.compare, name='mobile-compare')

]
