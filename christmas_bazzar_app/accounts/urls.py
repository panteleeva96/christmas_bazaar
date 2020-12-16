from django.urls import path, include

from accounts.views import signup_user, user_profile, signout_user

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', signup_user, name='sign up user'),
    path('profile/', user_profile, name='user profile'),
    path('signout/', signout_user, name='sign out user')
]