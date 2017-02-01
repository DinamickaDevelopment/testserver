# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Post(models.Model):
    """
    This model stores the posts
    """
    title = models.CharField(max_length=256, unique=True)
    short_title = models.CharField(max_length=64, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    text = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s (%s)' % (str(self.title), str(self.created))


class Contact(models.Model):
    """
    This model saves all contact form submissions
    """
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    company = models.CharField(max_length=128)
    phone = PhoneNumberField(blank=True)
    comment = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return u'Contact fromm %s %s @ %s' % (str(self.first_name), str(self.last_name), str(self.created))
