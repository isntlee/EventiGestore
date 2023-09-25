from django.contrib.auth.models import AbstractUser
from django_extensions.db.fields import AutoSlugField

class User(AbstractUser):
    slug = AutoSlugField(populate_from='username')
    pass