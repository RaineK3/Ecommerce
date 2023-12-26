from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about,name='about'),
    path('login_user/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('register_user/',views.register_user,name='register_user'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/<str:type>',views.category, name='category'),
]
