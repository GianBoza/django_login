from django.urls import path
from .views import RegisterView, LoginView, UserListCreate
# definicion de las rutas para manejar la navegacion
urlpatterns = [
    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/', UserListCreate.as_view(), name='user-list-create'),
]