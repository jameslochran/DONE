import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Project(models.Model):
    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")

    STATUSES = (
        ('to-do', ('To Do')),
        ('in_progress', ('In Progress')),
        ('blocked', ('Blocked')),
        ('done', ('Done')),
        ('dismissed', ('Dismissed'))
    )

    PRIORITIES = (
        ('00_low', ('Low')),
        ('10_normal', ('Normal')),
        ('20_high', ('High')),
        ('30_critical',('Critical')),
        ('40_blocker', ('Blocker'))
    )

    title = models.CharField(("title"), max_length=200)
    description = models.TextField(("description"), max_length=2000, null=True, blank=True)
    resolution = models.TextField(("resolution"), max_length=2000, null=True, blank=True)
    startdate = models.DateField(("start date"), null=True, blank=True)
    deadline = models.DateField(("deadline"), null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks_assigned', verbose_name=('assigned to'),
                                   on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(("state"), max_length=20, choices=STATUSES, default='to-do')
    priority = models.CharField(("priority"), max_length=20, choices=PRIORITIES, default='10_normal')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks_created', verbose_name=('created by'),
                                   on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(("created at"), auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(("last modified"), auto_now=True, editable=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "[%s] %s" % (self.id, self.title)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Item(models.Model):
    class Meta:
        verbose_name = ("Item")
        verbose_name_plural = ("Check List")

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    item_description = models.CharField(("description"), max_length=200)
    is_done = models.BooleanField(("done?"), default=False)

    def __str__(self):
        return self.item_description
