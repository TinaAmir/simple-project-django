from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , get_user_model , logout
from .forms import  RegisterForm , ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username, password = request.POST.get('username'), request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/ac/profile')
    return render(request,"accounts/login.html")

def register_view(request):
    context = {}
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.copy()
            password2 = data.pop('password2')
            user = get_user_model().objects.create_user(**data)
            return redirect('/ac/login')
        else:
            context['message'] = form.errors
    return render(request, "accounts/register.html",context)

@login_required(login_url=reverse_lazy('accounts:login'))
def profile_view(request):
    context = {}
    if request.method == "POST":
        data = request.POST.copy()
        data.update({
            "user" : request.user.id
        }   
        )
        form = ProfileForm(data)
        if form.is_valid():
            profile = form.save()
            
            return redirect('/')
            
        else :
            print(form.erors)
    return render(request,'accounts/profile.html',context)


def logout_view (request):
    logout(request)
    return redirect('/')
