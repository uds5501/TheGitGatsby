from django.db import models

# Create your models here.
class Developer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    following_count = models.PositiveIntegerField()
    follower_count = models.PositiveIntegerField()
    gists_count = models.PositiveIntegerField()
    avatar_url = models.URLField(max_length=500, unique=True)
    created_at = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return '@'+self.username


class Repository(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=4000)
    # using string of characters in <lang>:<size>, format
    languages = models.TextField(max_length=1000)
    stars = models.PositiveIntegerField()
    watchers = models.PositiveIntegerField()
    # from 0-51 indexing for the commits
    commit_history_week_wise = models.TextField(max_length=1000)
    owner = models.ForeignKey(Developer, related_name='repositories', on_delete=models.CASCADE)