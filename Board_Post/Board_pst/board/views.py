from django.shortcuts import redirect

from .forms import PostForm, RespondForm
from .models import Authors, Posts, Responds
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostsList(ListView):
    model = Posts
    ordering = '-date_create'
    template_name = 'board.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class PostDetail(DetailView):
    model = Posts
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['responds'] = Responds.objects.filter(post=self.object.id)
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = '/board/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Authors.objects.get(user=self.request.user)
        return super().form_valid(form)


class RespondCreate(LoginRequiredMixin, FormView):
    model = Responds
    form_class = RespondForm
    template_name = 'post_respond.html'
    context_object_name = 'respond'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Posts.objects.get(pk=self.request.GET.get('post_pk'))
        return context

    def post(self, request, *args, **kwargs):
        self.create_respond()
        return redirect(f'/board/{self.request.POST.get("post_pk")}')

    def create_respond(self):
        respond = Responds()
        respond.hater = Authors.objects.get(user=self.request.user)
        respond.post = Posts.objects.get(pk=self.request.POST.get('post_pk'))
        respond.text_respond = self.request.POST.get('text_respond')
        respond.save()

    def form_valid(self, form):
        return super().form_valid(form)


class RespondAccept(LoginRequiredMixin, ListView):
    model = Responds
    template_name = 'respond_accept.html'
    context_object_name = 'responds'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(post=self.request.GET.get('post_pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Posts.objects.get(pk=self.request.GET.get('post_pk'))


def respond_accept(request, *args, **kwargs):
    respond = Responds.objects.get(pk=request.GET.get('respond_id'))
    respond.accepted = True
    respond.accepted_notice = True
    respond.save()
    return redirect(f'/board/{respond.post.id}')


def respond_delete(request, *args, **kwargs):
    respond = Responds.objects.get(pk=request.GET.get('respond_id'))
    respond.deleted = True
    respond.deleted_notice = True
    respond.save()
    return redirect(f'/board/{respond.post.id}')


def subscribe(request, *args, **kwargs):
    if request.user.is_authenticated:
        subscribe_change(request.user, True)
    return redirect(f'/board/')


def unsubscribe(request, *args, **kwargs):
    if request.user.is_authenticated:
        subscribe_change(request.user, False)
    return redirect(f'/board/')


def subscribe_change(user, subscribe):
    author_user = Authors.objects.get(user=user)
    author_user.subscribers = subscribe
    author_user.save()












