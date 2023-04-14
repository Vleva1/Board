from django.db import models
from django.contrib.auth.models import User
import random


class PrivacySignature(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signature = models.IntegerField(default=0)
    date_create = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_privacy_signature(user):
        get_signature = PrivacySignature.objects.filter(user=user)
        if get_signature.exists():
            return get_signature[0].signature
        else:
            return None

    @staticmethod
    def new_privacy_signature(user: User):
        old_signature = PrivacySignature.objects.filter(user=user)
        for old in old_signature:
            old.delete()
        new_privacy_signature = random.randint(0, 100000)
        PrivacySignature(user=user, signature=new_privacy_signature).save()
        return new_privacy_signature






















