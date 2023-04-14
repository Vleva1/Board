from django.contrib.auth.models import User
from django.db import models

from . import resource


class Authors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    rate = models.IntegerField(default=0)
    subscribers = models.BooleanField(default=False)

    def __str__(self):
        return f'Имя автора: {self.user.username} - {self.rate}'


class Posts(models.Model):
    author = models.ForeignKey(Authors, null=True, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100, default='')
    post_text = models.TextField(default='')
    date_create = models.DateTimeField(auto_now_add=True)
    name_category = models.CharField(max_length=5, choices=resource.CATEGORIES_SELECT, default='')

    def __str__(self):
        return f'Публикация: {self.post_title} {self.post_text[:30]}... Автор: {self.author}'

    def preview(self):
        return f'{self.post_text[:125]}'


class Responds(models.Model):
    text_respond = models.TextField(default='', blank=True, null=True)
    date_respond = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, blank=True, null=True)
    hater = models.ForeignKey(Authors, on_delete=models.CASCADE, blank=True, null=True)
    accepted = models.BooleanField(default=False)
    accepted_notice = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    deleted_notice = models.BooleanField(default=False)

    def __str__(self):
        return f'Отклик: {self.id} - {self.text_respond}. {self.hater}'

    def send_accepted(self):
        return self.accepted_notice

    def sended_accepted(self):
        self.accepted_notice = False
        self.save()

    def send_deleted(self):
        return self.deleted_notice

    def sended_deleted(self):
        self.deleted_notice = False
        self.save()





