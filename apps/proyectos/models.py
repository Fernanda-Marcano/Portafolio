from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    name = models.CharField(verbose_name='Nombre del Proyecto', max_length=200, unique=True, blank=False, null=False)
    description = models.TextField(verbose_name='Descripción del Proyecto', blank=False, null=False)
    tecnology = models.CharField(verbose_name='Tecnología', max_length=200, blank=False, null=False)
    url = models.URLField(verbose_name='Url del Proyecto', max_length=200, blank=False, null=False)
    image = models.ImageField(verbose_name='Imagen del Proyecto', upload_to='img/', default='img/default_img.png')
    slug = models.SlugField(unique=True, blank=True, null=True)
    created = models.DateField(verbose_name='Fecha de creación', auto_now_add=True)
    
    class Meta:
        db_table = 'Proyectos'
        ordering = ['id', 'created']
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
    
    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
