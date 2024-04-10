from django.db import models
# Allows for generic relationships to make tags portable 
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length = 255)

class TaggedItem(models.Model):
    # which tag is applied to which object?
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
    # Type of object
    # ID of object
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()