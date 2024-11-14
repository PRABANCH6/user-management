from django.urls import path 
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('accounts/profile/home/about/', views.about_us, name='about'),
    path('contact/', views.contact, name='contact'),
    path('base/', views.base, name='base'),
    # path('logged_home/', views.my_login_view, name='logged_in_home'),
    path('accounts/profile/home', views.profile_home, name='profile_home'),
    path('logout/', views.user_logout, name='logout'),
    # path('accounts/profile/home/users/', views.list_user , name='list_user'),
    path('accounts/profile/home/users', views.list_user, name='users'),
    path('password_change/', views.password_change, name='password_change'),

    #add user  and update delete the users
    path('accounts/profile/home/users/add', views.add_user, name='add_user'),
    path('accounts/profile/home/delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path('accounts/profile/home/delete_user/<int:id>/', views.delete_user_confirm, name='delete_user_confirm'),
    path('accounts/profile/home/update_user/<int:id>/', views.update_user, name='update_user'), 
    path('accounts/profile/home/update_user/<int:id>/', views.update_user_confirm, name='update_user_confirm'),
    # path('accounts/profile/home/delete_user/<int:id>', views.delete_user, name='delete_user'),
    # password reset urls
    # path('accounts/password_reset/', include('django.contrib.auth.urls')),
    # path('accounts/password_reset/done/', views.password_reset_done, name='password_reset_done'),
    # # path('accounts/reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    # path('accounts/password_change/', views.password_change ,name='password_change'),
    # path('accounts/password_change/done/',views.password_change_done, name='password_change_done'),
    # path('accounts/reset/done/', views.password_reset_complete, name='password_reset_complete'),
    



    path('reset-password', PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
    path('reset-password/complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]