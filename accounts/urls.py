from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='admin/login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout")
]