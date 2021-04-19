from django.db import models
import re

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) <2:
            errors['first_name'] = "First Name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name must be at leaset 2 characters"
        if len(postData['password']) <6:
            errors['password'] = "Password must be at least 6 characters"
        if postData['password'] != postData['pw_confirm']:
            errors['password'] = "Passwords must match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = ("Invalid email address!")
        email_check = self.filter(email=postData['email'])
        if email_check:    
            errors['email'] = ("Email already in use")
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="static/images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class PostManager(models.Manager):
    def post_validator(self, postData):
        errors = {}
        if len(postData['post']) <1:
            errors['post'] = ("Post cannot be empty")
        return errors


class Wall_Post(models.Model):
    post=models.TextField()
    post_pic = models.ImageField(null=True, blank=True, upload_to="static/images/")
    poster=models.ForeignKey(User, related_name="user_posts", on_delete=models.CASCADE)
    users_like_wall_post = models.ManyToManyField(User, related_name='wall_post_liked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

class CommentManager(models.Manager):
    def comment_validator(self, postData):
        errors = {}
        if len(postData['comment']) < 1:
            errors['comment'] = ("Comment must be at least 1 character")
        return errors

class Comment(models.Model):
    comment = models.TextField()
    poster = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    wall_post = models.ForeignKey(Wall_Post, related_name="post_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

class Forum(models.Model):
    forum_post = models.TextField()
    poster = models.ForeignKey(User, related_name="user_forum_posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

class Forum_Comment(models.Model):
    answer = models.TextField()
    poster = models.ForeignKey(User, related_name="user_answers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()