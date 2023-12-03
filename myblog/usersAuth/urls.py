# blog/urls.py
from django.urls import path , include
from .views import login , signup

app_name = 'blog'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), 
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    # Add other URLs as needed
]
