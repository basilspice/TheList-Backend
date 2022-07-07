from django.urls import path
from .views.users import SignUp, SignIn, SignOut, ChangePassword
from .views.posts import PostsView, PostView
# from .views.comments import CommentsView, CommentView
urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('posts/<int:pk>', PostView.as_view(), name='posts'),
]