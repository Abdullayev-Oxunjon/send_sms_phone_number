from django.urls import path, include

from app.views.change_password_view import ChangePasswordView
from app.views.forgot_password_view import ForgotPasswordView, VerifyForgotPhoneNumberView
from app.views.login_view import LoginAPIView
from app.views.reigister_view import RegisterView
from app.views.verify_phone_number import VerifyPhoneNumberView

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("register-verify/", VerifyPhoneNumberView.as_view(), name='register-verify'),
    path("login/", LoginAPIView.as_view(), name='login'),
    path("change-password/", ChangePasswordView.as_view(), name='change-password'),
    path("forgot-password/", ForgotPasswordView.as_view(), name='forgot-password'),
    path("veriy-forgot-password/", VerifyForgotPhoneNumberView.as_view(), name='verify-forgot-password'),
]
