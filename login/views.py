from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.
from .forms import LoginForm
from .models import user

# def formView(request):
#     if request.session.has_key('username'):
#         username = request.session['username']
#         return render(request, 'loggedin.html', {'username': username})
#     else:
#         return render(request, 'login.html', {})


def loginView(request):
    if request.method == "POST":
        # username = "Wrong username or password"
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            try:
                u = user.objects.get(username=MyLoginForm.cleaned_data['username'])

            except:
                warning = 1
                return render(request, 'login.html', {'waring': warning})

            if MyLoginForm.cleaned_data['password'] == u.password:
                username = u.username
                request.session['username'] = username
                request.session.set_expiry(15);
                return HttpResponseRedirect(reverse('login:greeting'))

            else:
                warning = 1
                return render(request, 'login.html', {'waring': warning})


    else:
        return render(request, 'login.html', {})
        #     if MyLoginForm.cleaned_data['username'] == :
        #         if MyLoginForm.cleaned_data['password'] == '123':
        #             username = MyLoginForm.cleaned_data['username']
        #             request.session['username'] = username
        #             request.session.set_expiry(15);
        # return render(request, 'loggedin.html', {'username': username})

        # MyLoginForm = LoginForm()
        # return render(request, 'login.html', {})
        # formView(request)

def formView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'loggedin.html', {'username': username})
    else:
        return HttpResponseRedirect(reverse('login:login'))

def logoutView(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponse("Good bye!")
