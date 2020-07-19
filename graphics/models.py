import os
from django.db import models
from django.urls import reverse

class Tag(models.Model):
    tag = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return (self.tag)
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'

# a formset
class Graphics_Portfolio(models.Model):
    site_position =  (('------', '------'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))
    position = models.CharField(max_length=6,                              
    choices = site_position,                              
    default='------')
    tag = models.ManyToManyField(Tag, blank=False)
    description_header =  models.TextField(blank=False, null=False, max_length=1000)
    description_body =  models.TextField(blank=False, null=False, max_length=50000)
    image = models.FileField(upload_to='image')
    class Meta:
        verbose_name = "Graphics Portfolio"
        verbose_name_plural = 'Graphics Portfolio'
    def __str__(self):
        return str("position => {0} item".format(self.position))

class FinalDesigns(models.Model):
    portfolio = models.ForeignKey(Graphics_Portfolio, default=None, on_delete=models.CASCADE)
    final_design = models.ImageField(upload_to='finaldesign', verbose_name='Final Design Images')
    class Meta:
        verbose_name = "Final Design (IMG)"
        verbose_name_plural = 'Final Design (IMG)'

class Mocks(models.Model):
    portfolio = models.ForeignKey(Graphics_Portfolio, default=None, on_delete=models.CASCADE)
    mocks = models.ImageField(upload_to='mocks', verbose_name='Mocks Images')
    class Meta:
        verbose_name = "Mocks (IMG)"
        verbose_name_plural = 'Mocks (IMG)'


# a formset
class Graphics_Stack(models.Model):
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
class Graphics_Archive(models.Model):
    arch_position =  (('------', '------'), ('1', '1'), ('2', '2'), ('3', '3'), ('others','Others'))
    position = models.CharField(max_length=6,                              
    choices = arch_position,                              
    default='------')
    tag = models.ManyToManyField(Tag, blank=False)
    title = models.CharField(blank=False, null=False, max_length=5000 )
    description = models.CharField(blank=False, null=False, max_length=10000 )
    backend_tech = models.TextField(blank=False, null=False, max_length=5000 )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, help_text=""" 
          When django prepopulate slugs, it normally omits prepositions, do not forget
          to add it manually
        """) 
    def get_absolute_url(self):
        return reverse("graphics:detail",
        args = [self.slug
        ])

    class Meta:
        verbose_name = "Graphics Archive"
        verbose_name_plural = 'Graphics Archive'
    def __str__(self):
         return str("{0} with position => {1}".format(self.title, self.position))
    class Meta:
        ordering = ["-timestamp"]


class ArchiveFinalDesigns(models.Model):
    portfolio = models.ForeignKey(Graphics_Archive, default=None, on_delete=models.CASCADE)
    final_design = models.ImageField(upload_to='achieve/finaldesign', verbose_name='Archieve Final Design Images')
    class Meta:
        verbose_name = "Archieve Final Design (IMG)"
        verbose_name_plural = 'Archieve Final Design (IMG)'

class AchieveMocks(models.Model):
    portfolio = models.ForeignKey(Graphics_Archive, default=None, on_delete=models.CASCADE)
    mocks = models.ImageField(upload_to='achieve/mocks', verbose_name='Archieve Mocks Images')
    class Meta:
        verbose_name = "Archieve Mocks (IMG)"
        verbose_name_plural = 'Archieve Mocks (IMG)'



