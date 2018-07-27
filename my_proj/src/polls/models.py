import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Project(models.Model):

    to_do = 'To-Do'
    in_progress = 'In Progress'
    blocked = 'Blocked'
    done = 'Done'
    dismissed = 'Dismissed'
    STATUSES = (
        (to_do, 'To Do'),
        (in_progress, 'In Progress'),
        (blocked, 'Blocked'),
        (done, 'Done'),
        (dismissed, 'Dismissed')
     )

    project = models.CharField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(("description"), max_length=2000, null=True, blank=True)
    resolution = models.TextField(("resolution"), max_length=2000, null=True, blank=True)
    startdate = models.DateField(("start date"), null=True, blank=True)
    deadline = models.DateField(("deadline"), null=True, blank=True)
    date_created = models.DateTimeField(("date"), auto_now_add = True)
    date_changed = models.DateTimeField(("changed date"), auto_now = True)
    budget = models.IntegerField(("budget"), default=0.00)
    state = models.CharField(("state"), max_length=20, choices=STATUSES, default='To Do')



class Friend(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    current_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner', on_delete=models.CASCADE, null=True)

    # @classmethod
    # def make_friend(cls, current_user, new_friend):
    #     friend, create = cls.objects.get or create(
    #         current_user=current_user
    #     )
    #     friend.users.add(new_friend)
    #
    #
    # @classmethod
    # def lose_friend(cls, current_user, new_friend):
    #     friend, create = cls.objects.get or create(
    #     current_user=current_user
    # )
    #     friend.users.remove(new_friend)
    #







class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
