from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Authors, Responds



@receiver(post_save, sender=User)
def create_author(sender, instance, created, **kwargs):
    if not Authors.objects.filter(user=instance).exists():
        new_author = Authors(user=instance)
        new_author.save()


@receiver(post_save, sender=Responds)
def responds_notice(sender, instance: Responds, created, **kwargs):
    if not created:
        if instance.send_accepted():
            send_mail(
                subject=f'Отклик {instance.id}',
                message=f'Отклик на статью {instance} одобрен.',
                from_email='',
                recipient_list=[instance.hater.user.email]
            )
            instance.sended_accepted()

        if instance.send_deleted():
            send_mail(
                subject=f'Удаление отклика {instance.id}',
                message=f'Отклик на статью {instance} удален.',
                from_email='',
                recipient_list=[instance.hater.user.email]
            )
            instance.sended_deleted()
















