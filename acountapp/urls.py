from django.urls import path

from acountapp.views import hello_world

app_name = 'acountapp'

# 127.0.0.1:8000/acount/hello_world
# 함수 > accountapp:hello_world

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]