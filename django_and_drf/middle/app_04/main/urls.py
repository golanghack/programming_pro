from django.urls import path
from django.contrib.auth import views
from main.views import (index, other_page, AppLoginView,
                        profile, AppLogoutView, ChangeUserInfoView,
                        AppPasswordChangeView, RegisterUserView,
                        RegisterDoneView, user_activate, 
                        DeleteUserView)

app_name = 'main'
urlpatterns = [
    path('accounts/password_reset/', views.PasswordResetView.as_view(), 
                                                    name='password_reset'),
    path('accounts/password_reset/done', views.PasswordResetDoneView.as_view(), 
                                                    name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
                                                    name='password_reset_confirm'),
    path('accounts/reset/done/', views.PasswordResetCompleteView.as_view(), 
                                                    name='password_reset_complete'),
    path('accounts/register/activate/<str:sign>/', user_activate, 
                                    name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(),
                                            name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), 
                                            name='register'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), 
                                            name='change_user_info'),
    path('accounts/logout/', AppLogoutView.as_view(), name='logout'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), 
                                            name='profile_delete'),
    path('accounts/password/change', AppPasswordChangeView.as_view(), 
                                            name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', AppLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]