from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

# Create your models here.




class SiteSettings(SingletonModel):




    class Meta:
        verbose_name = _("Site Setting")
        verbose_name_plural = _("Site Settings")