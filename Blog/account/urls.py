from django.urls import path,include
from account.views import UserCreateView,profile_update_view,profile_page_view
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordChangeView,PasswordChangeDoneView

urlpatterns = [
    path('signup/',UserCreateView.as_view(), name='signup'),
    path('login/',LoginView.as_view(template_name = "account/login.html"),name = "login"),
    path('', include('django.contrib.auth.urls')),
    path('profile/',profile_page_view,name = 'profile'),
    path('profile-update/',profile_update_view,name = 'profile-update'),

    path('password_reset/',PasswordResetView.as_view(template_name="account/password_reset_form.html",email_template_name="account/password_reset_email.html"), name = 'password_reset'),
    path('password-reset/done/',PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name="account/password_confirm.html"), name = 'password_reset_confirm',),
    path('reset/done/',PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),

    path('password-change/',PasswordChangeView.as_view(template_name="account/password_change.html"), name='password_change'),
    path('password-change/done/',PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"), name='password_change_done'),

]