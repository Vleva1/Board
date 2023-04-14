from celery import shared_task
from .models import Authors, Posts
from django.utils.timezone import now
from datetime import timedelta, time, datetime
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_email_subscribers():
    for author in Authors.objects.all():
        today = datetime.now()
        period = 7
        start = datetime.combine(today - timedelta(days=period), time.max)
        finish = datetime.combine(today, time.min)
        last_weeks = Posts.objects.filter(date_create__range=[start, finish])

        if last_weeks:
            domain = settings.CURRENT_HOST
            html_content = render_to_string(
                'subscribe_email.html',
                {
                    'posted': last_weeks,
                    'domain': domain,
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'Новое за последнюю неделю',
                body='',
                from_email='',
                to=[author.user.email],
            )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()





