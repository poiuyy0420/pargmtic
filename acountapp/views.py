from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from acountapp.decorators import acount_ownership_required
from acountapp.forms import AcountUpdateForm
from acountapp.models import HelloWorld

has_ownership = [acount_ownership_required, login_required]

@login_required
def hello_world(request):
    # if request.user.is_authenticated:
    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('acountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'acountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    # else:
    #     return HttpResponseRedirect(reverse('acountapp:login'))


class AcountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('acountapp:hello_world')
    template_name = 'acountapp/create.html'


class AcountDeatilView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'acountapp/detail.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AcountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AcountUpdateForm
    success_url = reverse_lazy('acountapp:hello_world')
    template_name = 'acountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AcountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('acountapp:login')
    template_name = 'acountapp/delete.html'