from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Reply, Language, Profile
from .forms import PostForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

from taggit.models import Tag

from .langs_list import langs_list_str

"""
TODOS:

- Make sure the view increments reply count when a Reply is added
- TAG LOGIC!

"""



def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        # Make sure user exists
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username or password does not exist.')

        # Use Django's authenticate method, either returns error or User object with these credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log user in, add session in db/browser
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist.")

    context = {'page': page}

    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):

    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'base/home.html', context)


def post(request, username, pk):
    post = Post.objects.get(id=pk)
    post_replies = post.replies.all()
    

    if request.method == 'POST':
        reply = Reply.objects.create(
            author=request.user,
            body=request.POST.get('body'),
            parent_post=post
        )
        return redirect('post', username=post.author, pk=post.id)


    context = {
        'post': post,
        'post_replies': post_replies
    }
    
    return render(request, 'base/post.html', context)


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)

        if request.method == "POST":
            # Get current user ID
            current_user_profile = request.user.profile
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action == 'follow':
                current_user_profile.follows.add(profile)
            # Save profile
            current_user_profile.save()

        return render(request, 'base/profile.html', {"profile": profile})
    else:
        return redirect('home')

# For now just test to see if it works to render the language name etc.
def language_profile(request, pk):
    language = Language.objects.get(id=pk)
    # Make this if block a new post tagged with that language
    # if request.method == "POST":
        
    return render(request, 'base/language_profile.html', {"language": language})
    # else:
    #     return redirect('home')


@login_required(login_url='login')
def createPost(request):
    langs_list = langs_list_str.split(',')
    form = PostForm()
    if request.method == 'POST':

        # Get post body
        body = request.POST.get('body')

        # Get hashtags from post body
        hashtags = [word.strip('#') for word in body.split() if word.startswith('#')]

        # Get the language input
        language_input = request.POST.get('language')
        try:
            language = Language.objects.get(
                Q(name_english__icontains=language_input) | 
                Q(name_native__icontains=language_input)
            )
        except Language.DoesNotExist:
            # Incorporate this into Django messages, notifications, etc.
            return render(request, 'base/new_post.html', {'form': form, 'error_message': 'Language not found'})

        # Create the Post
        post = Post.objects.create(
            author=request.user,
            body=body,
            language=language  # Assuming you have a 'language' field in your Post model to store the language
        )

        for hashtag_text in hashtags:
            hashtag, created = Tag.objects.get_or_create(name=hashtag_text)
            post.tags.add(hashtag)


        return redirect('home')
    
    context = {
        'form': form,
        'langs_list': langs_list
    }
    return render(request, 'base/new_post.html', context)






@login_required(login_url='login')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.user != post.author:
        return HttpResponse("You are not allowed to do that!")
    
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': post})


@login_required(login_url='login')
def deleteReply(request, pk):
    reply = Reply.objects.get(id=pk)
    parent_post = reply.parent_post.id

    if request.user != reply.author:
        return HttpResponse("You are not allowed to do that!")

    if request.method == 'POST':
        reply.delete()
        return redirect('post', username=reply.parent_post.author, pk=parent_post)
    return render(request, 'base/delete.html', {'obj': reply})