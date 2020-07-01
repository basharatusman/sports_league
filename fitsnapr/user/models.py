from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        default='default.jpg', upload_to='profile_pics')
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    stripe_customer = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        profile_pic = Image.open(self.profile_picture.path)

        if profile_pic.height > 300 or profile_pic.width > 300:
            output_size = (300, 300)
            profile_pic.thumbnail(output_size)
            profile_pic.save(self.profile_picture.path)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return f'{self.user.username} profile'


class Address(models.Model):
    address1 = models.CharField(max_length=254, blank=True)
    address2 = models.CharField(max_length=254, blank=True)
    city = models.CharField(max_length=254, blank=True)
    provice = models.CharField(max_length=100, blank=True)
    post_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.post_code

    class Meta:
        verbose_name_plural = 'Address'


class BillingAddress(Address):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_profile.user.username}'s billing address"

    class Meta:
        verbose_name_plural = 'Billing Address'


class ShippingAddress(Address):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_profile.user.username}'s shipping address"

    class Meta:
        verbose_name_plural = 'Shipping Address'
