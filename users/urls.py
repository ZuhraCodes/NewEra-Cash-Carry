from django.urls import path
from users import api_endpoints

urlpatterns = [
    path("login/", api_endpoints.NewLoginAPIView.as_view(), name="login-user"),
    path('login/confirm/', api_endpoints.NewLoginConfirmAPIView.as_view(), name="confirm-login-user"),
]