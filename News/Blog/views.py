import urllib.parse

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from Blog.algoritm import *
from Blog.forms import RegisterUserForm, LoginUserForm, AddPageForm, CreateProfileForm
from Blog.models import Post, Comment, Profile, Category


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/single_post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'




class HomeView(ListView):
    model = Post
    paginate_by = 14
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class PostListViewForCategory(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    extra_context = {'title': 'Категории'}
    def get_queryset(self):
            return Post.objects.select_related('category').filter(category__slug=self.kwargs.get("slug"))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Посты Категории: {Category.objects.get(slug=self.kwargs.get("slug"))}'
        return context


class PostListViewForUser(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'


    def get_queryset(self):
        return Post.objects.select_related('author').filter(author__pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Посты пользователя: {Profile.objects.get(pk=self.kwargs.get("pk"))}'
        return context
def get_cats(request):
    return render(request, 'blog/show_category.html')

class ProfileView(DetailView):
    model = Profile
    template_name = 'blog/profile.html'
    context_object_name = 'profile'
    slug_url_kwarg = 'pk'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_post'] = Post.objects.filter(author=self.kwargs.get("pk")).count()
        if self.request.user.is_authenticated:
            if Profile.objects.get(user=self.request.user.pk).pk == self.kwargs.get("pk"):
                context['logout'] = 1
            else:
                context['logout'] = 0
        else:
            context['logout'] = 0
        return context
def create_comment(request, pk):
    if request.user.is_authenticated:
        if request.method=="POST":
            comment = Comment()
            comment.post_id = pk
            comment.author_id = Profile.objects.get(user=request.user.pk).pk
            comment.image = Profile.objects.get(user=request.user.id)
            comment.message = request.POST['message']
            comment.save()
            return redirect(Post.objects.get(pk=pk).get_absolute_url())
    else:
        return redirect('login')

class AddPostView(CreateView):
    form_class = AddPageForm
    template_name = 'blog/addpost.html'
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            post = form.save(commit=False)
            post.author_id = Profile.objects.get(user=self.request.user.pk).pk
            post.slug = slugify(form.cleaned_data['name'])
            post.save()
            return redirect('profile_url', pk=post.author_id)
        else:
            return redirect('login')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'profile/register.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('create_profile', pk=user.pk)

def update_profile(request):
    now_profile = get_object_or_404(Profile, user=request.user.pk)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateProfileForm(request.POST, instance=now_profile)
            if form.is_valid():
                post = form.save(commit=False)
                post.user_id = request.user.pk
                post.save()
                return redirect('profile_url', pk=Profile.objects.get(user=request.user).pk)
        else:
            form = CreateProfileForm( instance=now_profile)
        return render(request, 'blog/create_profile.html', context={'bottom_name': 'edit', 'form': form})
    else:
        return redirect('login')
class CreateProfile(CreateView):
    form_class = CreateProfileForm
    template_name = 'blog/create_profile.html'
    def form_valid(self, form):
            profile = form.save(commit=False)
            profile.user_id = self.kwargs.get('pk')
            account = profile.save()
            login(self.request, User.objects.get(pk=profile.user_id))
            return redirect('home_url')

class LoginUser(LoginView):#класс входа пользователя
    form_class = LoginUserForm
    template_name = 'profile/login.html'

    def get_success_url(self):#переправляет нас на главную страницу в случае успешного входа в систему
        return reverse_lazy('home_url')

def post_search(request):
    search = request.GET.get('search', False)
    context = {}
    if search:
        posts = get_valide_post(Post.objects.all(), search)
        context = {'posts': posts, 'search_words':search}
    return render(request, 'blog/search.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')

# def get_email(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         send_email(email)
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
