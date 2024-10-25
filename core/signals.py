from django.db.models.signals import post_save
from django.dispatch import receiver

from core import models
from core import common_config


    
@receiver(post_save, sender=models.Company)
def create_default_units(sender, instance, created, **kwargs):
    if created:
        for unit_name, unit_description in common_config.default_units:
            models.Unit.objects.create(name=unit_name, company=instance, description=unit_description)
            