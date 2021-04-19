from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Wall_Post, Comment, Forum, Forum_Comment
import bcrypt


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect("/dashboard")
            messages.error(request, "Incorrect email and/or password")
        else:
            messages.error(request, "Email could not be found")
    return redirect('/')

def register(request):
    return render(request, 'register.html')

def registration(request):
    if request.method == "GET":
        return redirect('/')
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=pw_hash
            )
            request.session['user_id'] = user.id
            messages.success(request, "Successfully registered!")
            return redirect('/dashboard')
    return redirect('/register')

def dashboard(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "wall_posts": Wall_Post.objects.all()

    }
    return render(request, 'dashboard.html', context)

def add_post(request):
    if request.method == "POST":
        errors = Wall_Post.objects.post_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Wall_Post.objects.create(
                post=request.POST['post'],
                poster=User.objects.get(id=request.session['user_id']),
            )
    return redirect('/dashboard')

def post_comment(request, wall_post_id):
    if request.method == "POST":
        errors = Comment.objects.comment_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Comment.objects.create(
                comment=request.POST['comment'],
                poster=User.objects.get(id=request.session['user_id']),
                wall_post=Wall_Post.objects.get(id=wall_post_id)
            )
    return redirect('/dashboard')

def delete_post(request, wall_post_id):
    if request.method == "POST":
        post = Wall_Post.objects.get(id=wall_post_id)
        post.delete()
    return redirect('/dashboard')

def delete_comment(request, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
    return redirect('/dashboard')

def like_wall_post(request, wall_post_id):
    if 'user_id' in request.session:
        wall_post = Wall_Post.objects.get(id=wall_post_id)
        wall_post.users_like_wall_post.add(User.objects.get(id=request.session['user_id']))
        wall_post.save()
        return redirect('/dashboard')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def profile(request, profile_id):
    context = {
        "user": User.objects.get(id=profile_id)
    }
    return render(request, 'profile.html', context)

def forum(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        # "forum_posts": Forum.objects.all()
    }
    return render(request, 'forum.html', context)

# def add_forum_post(request):
#     if request.method == "POST":
#         errors = Wall_Post.objects.post_validator(request.POST)
#         if len(errors) > 0:
#             for key, value in errors.items():
#                 messages.error(request, value)
#         else:
#             Forum.objects.create(
#                 forum_post=request.POST['post'],
#                 poster=User.objects.get(id=request.session['user_id']),
#             )
#     return redirect('/forum')
