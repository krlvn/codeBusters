from django.urls import path
import userapp.views as userapp


app_name = 'userapp'


urlpatterns = [
    path('login/', userapp.login, name='login'),
    path('logout/', userapp.logout, name='logout'),
    path('register/', userapp.register, name='register'),
]
