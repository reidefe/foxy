from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.OneToOneField(User, verbose_name=_(""), on_delete=models.CASCADE)
    description = models.CharField(_(""), max_length=50)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class NewsModel(models.Model):
    heading = models.CharField(_("heading of news"), max_length=50)
    body = models.TextField(verbose_name=_("content of news article"), max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading
