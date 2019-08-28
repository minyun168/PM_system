from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """log out"""
    logout(request)
    return HttpResponseRedirect(reverse('PM:index'))

def register(request):
    """User register"""
    if request.method != 'POST':
        # empty register form 
        form = UserCreationForm()
    else:
        # handle fill in form 
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # auto log in and redirect
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('PM:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
