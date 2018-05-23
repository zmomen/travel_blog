from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template import RequestContext

from accounts.forms import RegistrationForm, EditProfileForm

from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth import update_session_auth_hash, authenticate, login

from home.models import Blog


def login_redirect(request):
    return redirect('accounts:login')
    # return render(request, 'accounts/login.html', {'test': 'this is purley test'})


def login_user(request):
    blogs = Blog.objects.filter(public=True).order_by('-created')[:3]
    args = {'blogs': blogs}

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
                login(request, user)
                return redirect('home:home')
        else:
            form = AuthenticationForm()
            args['errors'] = 'Invalid username or password!'
            args['form'] = form
            return render(request, 'accounts/login.html', args)

    else:
        form = AuthenticationForm()
        args['form'] = form
        return render(request, 'accounts/login.html', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
        else:
            return render(request, 'accounts/reg_form.html', {'form': form, 'errors': 'Form error!'})
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    args = {'user': user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:view_profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:view_profile')
        else:
            redirect('accounts:change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

