from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from acountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('acountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'acountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AcountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('acountapp:hello_world')
    template_name = 'acountapp/create.html'
