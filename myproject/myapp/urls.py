from django.urls import path
from .views import RegisterView, LoginView, UserListCreate, AttendanceView

urlpatterns = [
    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('attendance/', AttendanceView.as_view(), name='attendance'),
]