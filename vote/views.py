from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from home.context_processors import dashboard
from home.models import Blog
from vote.models import Activity, get_my_favorites


# Create your views here.


def upvote(request, blog_pk=None):
    if request.method == 'POST':
        blog = Blog.objects.get(pk=request.POST['pk'])
        blog.upvote +=1
        blog.save()

        data = {
            'vote': blog.upvote
        }
        return JsonResponse(data)
    if request.method == 'GET':
        blog = Blog.objects.get(pk=blog_pk)
        blog.upvote += 1
        blog.save()
        return redirect('home:all_blogs')


def favorite(request, fave=None, blog_pk=None):
    if request.method == 'POST':
        blog = Blog.objects.get(pk=blog_pk)
        print('favoritehere', fave, blog)
        if fave == 'F':
            a = Activity.objects.create(user=request.user, activity_type='F', blog=blog)
            print('activity created', a)
        elif fave == 'U':
            a = Activity.objects.filter(user_id=request.user.id, blog_id=blog_pk).delete()
            print('activity deleted', a)
        return redirect('vote:show_favorites')


def show_favorites(request):
    if request.method == 'GET':
        my_favorites = get_my_favorites(request.user)
        args = {'my_favorites': my_favorites}
        dash = dashboard(request)

        args = dict(args, **dash)
        return render(request, 'vote/my_favorites.html', args)


def add_tag(request, blog_pk=None):
    if request.method == 'POST':
        print('adding tag here', request.POST['newTag'], 'for ', blog_pk)
        tag_name = request.POST['newTag']
        blog = Blog.objects.get(pk=blog_pk)
        blog.tags.add(tag_name)
        blog.save()
        return redirect('/home/blog/'+blog_pk)


def change_tag(request, action=None, blog_pk=None, tag_name=None):
    if action == 'a' and request.method == 'POST':
        print('action is ', action, ' tag ', tag_name, request.POST['newTag'], 'blog ', blog_pk)
        tag_name = request.POST['newTag']
        blog = Blog.objects.get(pk=blog_pk)
        blog.tags.add(tag_name)
        blog.save()
        return redirect('/home/blog/' + blog_pk)

    elif action == 'r':
        print('action is ', action, ' tag ', tag_name, 'blog ', blog_pk)
        blog = Blog.objects.get(pk=blog_pk)
        blog.tags.remove(tag_name)
        blog.save()
        return redirect('/home/blog/' + blog_pk)