from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
global prices_dict



prices_dict = {'BEGINNER': 49, "INTERMEDIATE": 79, "PROFESSIONAL":99}

class Package(models.Model):

    package_choices = (
        ('BEGINNER', 'Beginner'),
        ("INTERMEDIATE", 'Intermediate'),
        ("PROFESSIONAL", 'Professional'),
    )

    package_type = models.CharField(
        max_length = 20,
        choices = package_choices,
        default = 'BEGINNER',
    )

    price = models.IntegerField(default = 0, null = True)

    def get_price(self):
        price = prices_dict.get(self.package_type)
        self.price = price
        self.save()
        print(self.price)


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300,null=True)
    phone = models.CharField(max_length=12,null = True)
    purchased = models.NullBooleanField(null = True,default = False)
    package = models.ForeignKey(Package,null=True)

    def __str__(self):
        return self.name

class Developer(models.Model):
    user = models.OneToOneField(User,null = True)
    company = models.ForeignKey(Company,null =True)



















class Post(models.Model):
    author = models.ForeignKey('auth.User',null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
