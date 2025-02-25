from django.urls import path
from .views import home, register, user_login, user_logout  # Import login view


urlpatterns = [
    path('', home, name='home'),  # Home page URL
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),  # Login page
    path('logout/', user_logout, name='logout'),  # Home page URL
]
