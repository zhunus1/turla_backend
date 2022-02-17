from django.urls import path
from .views import (
    HandShakeView,
    SignInView,
    SignUpView,
)

urlpatterns = [
    path('handshake/', HandShakeView.as_view(), name='handshake'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
]
