from django.contrib.auth.models import User

from home.models import Friend, Blog
from vote.models import get_my_favorites

from django.contrib.auth.decorators import login_required




@login_required
def dashboard(request):
    if request.user.is_authenticated:
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        my_blog_count = Blog.objects.filter(user=request.user).count()

        others = users.count() - friends.count()
        if get_my_favorites(request.user) is not None:
            my_faves = [blog.pk for blog in get_my_favorites(request.user)]
        else:
            my_faves = []

        return {'users': users, 'friends': friends,
                'my_blog_count': my_blog_count, 'my_faves': my_faves, 'others': others}
    else:
        return None


