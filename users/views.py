from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from users.forms import SignUpForm


# Create your views here.
def register(request): 
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
            
    else: 
        form = SignUpForm()

    context = {'form' : form}
    return render(request, 'registration/signup.html', context)