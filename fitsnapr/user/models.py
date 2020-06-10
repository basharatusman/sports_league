from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        default='default.jpg', upload_to='profile_pics')
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    class Meta:
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        profile_pic = Image.open(self.profile_picture.path)

        if profile_pic.height > 300 or profile_pic.width > 300:
            output_size = (300, 300)
            profile_pic.thumbnail(output_size)
            profile_pic.save(self.profile_picture.path)


class Address(models.Model):
    address1 = models.CharField(max_length=254, blank=True)
    address2 = models.CharField(max_length=254, blank=True)
    city = models.CharField(max_length=254, blank=True)
    provice = models.CharField(max_length=100, blank=True)
    post_code = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name_plural = 'Address'

    def __str__(self):
        return self.post_code


class BillingAddress(Address):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Billing Address'

    def __str__(self):
        return f"{self.userprofile.user_id}'s billing address"


class ShippingAddress(Address):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Shipping Address'

    def __str__(self):
        return f"{self.userprofile.user_id}'s shipping address"
