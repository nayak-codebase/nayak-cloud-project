from django.db import models
from django.conf import settings

# Create your models here.
class FileItem(models.Model):
    user                            = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.DO_NOTHING,)
    name                            = models.CharField(max_length=120, null=True, blank=True)
    url				    = models.URLField(null=True, blank=True)
    description                     = models.TextField(blank=True, null=True)
    path                            = models.TextField(blank=True, null=True)
    download                        = models.URLField(null=True, blank=True)
    size                            = models.BigIntegerField(default=0)
    file_type                       = models.CharField(max_length=120, null=True, blank=True)
    timestamp                       = models.DateTimeField(auto_now_add=True)
    updated                         = models.DateTimeField(auto_now=True)
    uploaded                        = models.BooleanField(default=False)
    active                          = models.BooleanField(default=True)
    @property
    def title(self):
        return str(self.name)
