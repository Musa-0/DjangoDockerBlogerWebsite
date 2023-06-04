from django.urls import path
from django.views.decorators.cache import cache_page

from Blog.views import *

urlpatterns = [
    path('addpost/', AddPostView.as_view, name='addpost'),
    path('update_profile/', update_profile, name='update_profile'),
    path('create_profile/<int:pk>', CreateProfile.as_view(), name='create_profile'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile_url'),
    # path('your_email/', get_email, name='your_email'), временно заброшенно
    path('login/',LoginUser.as_view(), name='login'),
    path('register/',RegisterUser.as_view(), name='register'),
    path('search_post/', post_search, name='post_search'),
    path('logout/', logout_user, name='logout'),
    path('category/', get_cats, name='show_all_category'),#!!!!!!
    path('comment/<int:pk>/',create_comment, name='create_comment'),
    path('post_ditail/<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name='post_single_url'),
    path('category_post/<slug:slug>', cache_page(60 * 100)(PostListViewForCategory.as_view()), name='post_list_url'),
    path('user_post/<int:pk>', PostListViewForUser.as_view(), name='post_list_user_url'),
    path('',HomeView.as_view(), name='home_url'),
]
