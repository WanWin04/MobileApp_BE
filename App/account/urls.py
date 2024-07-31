from django.urls import path
from .views import RegisterView
from rest_framework.authtoken import views as authviews


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('api-token-auth/', authviews.obtain_auth_token, name='api-token-auth'),
]
