from django.db import models
from django.contrib.auth.models import User

from home.models import Blog


# Create your models here.
class Activity(models.Model):
    FAVORITE = 'F'
    LIKE = 'L'
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPES = (
        (FAVORITE, 'Favorite'),
        (LIKE, 'Like'),
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    activity_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE)


def get_my_favorites(current_user):
    my_faves = list()
    for b in Activity.objects.filter(user_id=current_user.id):
        my_faves.append(b.blog)
    my_faves = sorted(my_faves, key=lambda x: x.created, reverse=True)

    return my_faves

