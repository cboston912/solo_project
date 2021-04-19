from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('registration', views.registration),
    path('dashboard', views.dashboard),
    path('profile/<int:profile_id>', views.profile),
    path('logout', views.logout),
    path('add_post', views.add_post),
    path('post_comment/<int:wall_post_id>', views.post_comment),
    path('delete_post/<int:wall_post_id>', views.delete_post),
    path('delete_comment/<int:comment_id>', views.delete_comment),
    path('like/<int:wall_post_id>', views.like_wall_post),
    path('forum', views.forum),
    # path('add_forum_post', views.add_forum_post),

]