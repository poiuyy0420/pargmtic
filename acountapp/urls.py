from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from acountapp.views import hello_world, AcountCreateView, AcountDeatilView, AcountUpdateView

app_name = 'acountapp'

# 127.0.0.1:8000/acount/hello_world
# 함수 > acountapp:hello_world

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='acountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AcountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AcountDeatilView.as_view(), name='detail'),
    path('update/<int:pk>', AcountUpdateView.as_view(), name='update'),



]