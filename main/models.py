import os
from django.db import models


# a formset
class Portfolio(models.Model):
    site_position =  (('------', '------'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))
    position = models.CharField(max_length=6,                              
    choices = site_position,                              
    default='------')
    description_header =  models.TextField(blank=False, null=False, max_length=1000)
    description_body =  models.TextField(blank=False, null=False, max_length=50000)
    image = models.FileField(upload_to='image')
    github = models.CharField(blank=False, null=False, max_length=5000 )
    link = models.CharField(blank=False, null=False, max_length=5000 )
    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = 'Portfolio'
    def __str__(self):
        return str(self.github)


# a formset
class Stack(models.Model):
    stack_position =  (('------', '------'), ('1', '1'), ('2', '2'), ('3', '3'), ('others','Others'))
    position = models.CharField(max_length=6,                              
    choices = stack_position,                              
    default='------')
    icon = models.FileField(upload_to='stack_image')
    tech = models.CharField(blank=False, null=False, max_length=5000 )
    about_tech = models.TextField(blank=False, null=False, max_length=5000 )
    link = models.CharField(blank=False, null=False, max_length=2000)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = "Stack"
        verbose_name_plural = 'Stack'
        ordering = ["-timestamp"]
    def __str__(self):
        return str(self.tech)


# a formset
class Archive(models.Model):
    arch_position =  (('------', '------'), ('1', '1'), ('2', '2'), ('3', '3'), ('others','Others'))
    position = models.CharField(max_length=6,                              
    choices = arch_position,                              
    default='------')
    github = models.CharField(blank=False, null=False, max_length=5000 )
    external_link = models.CharField(blank=False, null=False, max_length=5000 )
    title = models.CharField(blank=False, null=False, max_length=5000 )
    description = models.CharField(blank=False, null=False, max_length=10000 )
    backend_tech = models.TextField(blank=False, null=False, max_length=5000 )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = "Archive"
        verbose_name_plural = 'Archive'
    def __str__(self):
        return str(self.title)
    class Meta:
        ordering = ["-timestamp"]


class Contact(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    subject = models.CharField(max_length=220, blank=False, null=False)
    email = models.EmailField(max_length=60, blank=False, null=False)
    message = models.TextField(max_length=90000, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-timestamp"]


