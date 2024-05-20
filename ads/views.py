from datetime import timezone

import pytz
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
# from ads.forms import ImageForm
from .models import *
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView,DeleteView
)
from .forms import PostForm
from django.urls import reverse_lazy
class PostList(ListView):
    queryset = Post.objects.order_by('time_in')
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

# прописываю функции для выбора таймзоны
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = timezone.localtime(timezone.now())
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/posts/')


class PostDetail(DetailView):
    queryset = Post.objects.all()
    template_name = 'post.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = timezone.localtime(timezone.now())
        context['timezones'] = pytz.common_timezones
        return context
    def post(self, request, pk):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect(f'/posts/{pk}')
class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
    # def post(self, request):
    #     request.session['django_timezone'] = request.POST['timezone']
    #     return redirect('/posts/')
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# # для отражения изображения
#
# def image_upload_view(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'index.html', {'form': form})