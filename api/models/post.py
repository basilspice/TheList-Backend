from django.db import models
from django.contrib.auth import get_user_model
from sqlite3 import Date
from django.conf import settings
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
  return 'posts/{filename}' .format(filename=filename)

class Post(models.Model):
  title = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  content = models.CharField(max_length=500)
  created_at = Date.today()
  author = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  image = models.ImageField(_("Image"), upload_to=upload_to, default='posts/default.jpg' )
  def __str__(self):
    # This must return a string
    return f"blogging is just the best {self.title}"   