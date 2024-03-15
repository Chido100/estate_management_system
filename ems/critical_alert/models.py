from django.db import models
from users.models import User
from twilio.rest import Client
from django.conf import settings
from decouple import config



class CriticalAlert(models.Model):
    alert = models.TextField(default='Please Help!!!')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alert_sender')
    #receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alert_receiver', default='01')
    date_sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_sent']
        verbose_name_plural = 'Critical Alert'

    def __str__(self):
        return f'{self.sender.username}'

    
    def save(self, *args, **kwargs):

        if self.alert:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

            message = client.messages.create(
                body=self.alert,
                from_= config('MY_TWILIO_PHONE_NUMBER'),
                    to=config('RECIPIENT_NUMBER')
            )

            print(message.sid)
        return super().save(*args, **kwargs)







