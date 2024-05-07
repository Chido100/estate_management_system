from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image



class AllStreets(models.Model):
    street = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'All Streets'

    def __str__(self):
        return self.street
    
class HouseNumbers(models.Model):
    house = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'House Numbers'

    def __str__(self):
        return self.house



class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, default='')
    house_number = models.ForeignKey(HouseNumbers, on_delete=models.CASCADE, related_name='houses', default='00')
    street_name = models.ForeignKey(AllStreets, on_delete=models.CASCADE, related_name='all_streets', default='street')
    phone_number = PhoneNumberField(blank=True, null=True)
    
    #approval_status = models.CharField(max_length=20, choices=APPROVAL_STATUS, default='Pending')

    is_resident = models.BooleanField(default=False)
    is_security = models.BooleanField(default=False)
    is_management = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.user.username} Profile'

