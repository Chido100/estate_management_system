from django.db import models
from users.models import User


class NewMail(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE, default='')


    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'New Mail'

    def __str__(self):
        return self.subject


class ReplyMail(models.Model):
    new_subject = models.ForeignKey(NewMail, editable=False, on_delete=models.CASCADE, related_name='new_mail_subject')
    new_content = models.ForeignKey(NewMail, editable=False, on_delete=models.CASCADE, related_name='new_mail_content')
    reply_message = models.TextField()
    date_replied = models.DateTimeField(auto_now_add=True)
    reply_by = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.new_subject






