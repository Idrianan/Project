from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, ThemeCreateForm, PostCreateForm
from .models import Forums,Themes, Post

@login_required
def dashboard(request):
    Forumss = Forums.objects.all()
    return render(request, 'account/dashboard.html', {'Forumss': Forumss})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Авторизация успешна')
                else:
                    return HttpResponse('Авторизация невозможна')
            else:
                return HttpResponse('Неверный логин')
    else:
        form = LoginForm()
    return render(request, 'account/registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/registration/register.html', {'user_form': user_form})


def logging_out(request):
    logout(request)
    return render(request,'account/registration/logged_out.html')

@login_required
def forum(request, slug):
    Themess = Themes.objects.all()
    Forumss = Forums.objects.all()
    for i in Forumss:
        if i.name == slug:
            cur_forum = i
    if request.method == 'POST':
        theme_form = ThemeCreateForm(request.POST)
        if theme_form.is_valid():
            cur_user = request.user
            for i in Forums.objects.all():
                if i.name == slug:
                    task = i
            theme_form.forum_id = task.id
            theme_form.start_msg_usr_id=cur_user.id
            neww_theme = theme_form.save(commit=False)
            neww_theme.forum_id = task
            neww_theme.start_msg_usr_id=cur_user
            neww_theme.save()
            return render(request, 'account/forum/index.html', {'neww_theme': neww_theme, 'Themess': Themess, 'theme_form': theme_form, 'slug': slug, 'cur_forum': cur_forum})
    else:
        theme_form = ThemeCreateForm()
    return render(request, 'account/forum/index.html', {'theme_form': theme_form, 'slug': slug, 'Themess': Themess, 'cur_forum': cur_forum})

@login_required
def themes(request,slug):
    Themess = Themes.objects.all()
    Posts = Post.objects.all()
    for i in Themess:
        if i.name == slug:
            cur_theme = i
    if request.method == 'POST':
        post_form = PostCreateForm(request.POST)
        if post_form.is_valid():
            cur_user = request.user
            for i in Themes.objects.all():
                if i.name == slug:
                    task = i
            neww_theme = post_form.save(commit=False)
            neww_theme.theme_id = task
            neww_theme.sender_id=cur_user
            neww_theme.save()
            return render(request, 'account/theme/index.html', {'neww_theme': neww_theme, 'post_form': post_form, 'slug': slug, 'Posts': Posts, 'cur_theme': cur_theme})
    else:
        post_form = PostCreateForm()
    return render(request, 'account/theme/index.html', {'post_form': post_form, 'slug': slug, 'Posts': Posts,'cur_theme': cur_theme})