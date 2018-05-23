from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from home.forms import BlogForm, CommentForm
from home.models import Blog, Friend

from home.context_processors import dashboard


class HomeView(TemplateView):
    template_name = 'home/home.html'

    # render the form when we have a get request.
    def get(self, request):
        form = BlogForm()
        blogs = Blog.objects.filter(public=True).order_by('-created', '-upvote')[:3]

        args = {'form': form, 'blogs': blogs}
        dash = dashboard(request)
        args = dict(args, **dash)

        return render(request, self.template_name, args)
    #
    # @staticmethod
    # def post(request):
    #     form = BlogForm(request.POST)
    #     if form.is_valid():
    #         blog = form.save(commit=False)
    #         blog.user = request.user
    #         blog.save()
    #         return redirect('home:home')
    #     else:
    #         return render(request, 'home/home.html', {'form': form, 'errors': 'Form error!'})


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:home')


def search(request):
    if request.method == 'POST':
        query = request.POST['q']
        if query:
            # search blogs:
            blogs_q = (Blog.objects.filter(public=True, blog__icontains=query) |
                       Blog.objects.filter(public=True, title__icontains=query) |
                       Blog.objects.filter(tags__name__contains=query)).distinct()

            # sort by upvoted.
            blogs_q = blogs_q.order_by('-upvote', '-created')

            # search users:
            users = User.objects.filter(username__icontains=query) | User.objects.filter(
                first_name__icontains=query) | \
                    User.objects.filter(last_name__icontains=query).order_by('-last_login')

            args = {'query': query, 'blogs': blogs_q, 'users': users}
            return render(request, 'home/search_results.html', args)
        else:
            return render(request, 'home/search_results.html', {'errors': 'You did not type anything!', 'query': query})


def search_nlp(request, sort=None):
    if request.method == 'POST':
        query = request.POST['qry']
        file = open('stopwords.txt', 'r')

        noise = file.read().splitlines()

        new_q = []
        for word in query.split(" "):
            if word in noise:
                continue
            else:
                new_q.append(word)

        print('NLI terms', new_q)

        if len(new_q) > 0 and new_q[0] != '':

            blogs_q = Blog.objects.none()
            for e in new_q:
                # search blogs:
                blogs_q = blogs_q | (Blog.objects.filter(public=True, blog__icontains=e) |
                                     Blog.objects.filter(public=True, title__icontains=e) |
                                     Blog.objects.filter(tags__name__contains=e)).distinct()

            # sort by favorites = 'faves'
            blogs_q = blogs_q.annotate(faves=Count('activity'))

            # determine sort
            blogs_q = blogs_q.order_by('-upvote', '-created', '-faves')

            # search users:
            users = User.objects.filter(username__icontains=new_q[0]) | User.objects.filter(
                first_name__icontains=new_q) | \
                    User.objects.filter(last_name__icontains=new_q[0]).order_by('-last_login')

            args = {'query': new_q, 'blogs': blogs_q, 'users': users}
            dash = dashboard(request)
            args = dict(args, **dash)
            return render(request, 'home/search_results.html', args)
        else:
            args = {'errors': 'You did not type anything!', 'query': new_q}
            dash = dashboard(request)
            args = dict(args, **dash)
            return render(request, 'home/search_results.html', args)


def all_blogs(request):
    if request.method == 'GET':
        blogs = Blog.objects.filter(public=True).exclude(user=request.user).order_by('-upvote', '-created')

        if blogs.count() == 0:
            errors = 'There are no blogs.'

        args = {'blogs': blogs}
        dash = dashboard(request)
        args = dict(args, **dash)
        return render(request, 'home/all_blogs.html', args)


def create_blog(request):
    if request.method == 'POST':
        print('creating...')
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('home:view_blog')
        else:
            return render(request, 'home/create_blog.html', {'form': form, 'errors': 'Form error!'})
    else:
        form = BlogForm()
        args = {'form': form}
        dash = dashboard(request)
        args = dict(args, **dash)
        return render(request, 'home/create_blog.html', args)


def view_blog(request, pk=None, all=None):
    form = errors = ''
    if request.method == 'GET':
        if pk:
            blogs = Blog.objects.filter(pk=pk)
        elif all:
            blogs = Blog.objects.all().order_by('-updated')
        else:
            blogs = Blog.objects.filter(user=request.user).order_by('-updated')

        if blogs.count() == 0:
            errors = 'You have no blogs.'
            form = BlogForm()

        commentForm = CommentForm()
        args = {'blogs': blogs, 'form': form, 'errors': errors, 'commentForm': commentForm}
        dash = dashboard(request)
        args = dict(args, **dash)

        return render(request, 'home/blog.html', args)


def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)

        if form.is_valid():
            form.save()
            return redirect('home:view_blog_with_pk', pk)
        else:
            form = BlogForm(instance=blog)
            args = {'form': form, 'error': 'Something is wrong!'}

            return render(request, 'home/edit_blog.html', args)
    else:
        form = BlogForm(instance=blog)
        args = {'form': form}
        dash = dashboard(request)
        args = dict(args, **dash)

        return render(request, 'home/edit_blog.html', args)


def add_blog_comment(request, pk=None):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print('im adding', form)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            return redirect('home:view_blog_with_pk', pk)
        else:
            print('invald form')
            redirect('home:home')
    else:
        return redirect('home:home')
