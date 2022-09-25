from email.policy import default
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField 

# Create your models here.
class Cmspage(models.Model):
    title=models.CharField(max_length=200,verbose_name="Name")
    slug=models.SlugField(max_length=100,allow_unicode=True)
    image_name = models.CharField(max_length=140, blank=True,verbose_name="Banner alt")
    banner = models.ImageField(upload_to='images/',default='')
    description = RichTextField()
    meta_title=models.CharField(max_length=200,blank=True,verbose_name="Meta Title")
    meta_desc=models.CharField(max_length=200,blank=True,verbose_name="Meta Description")
    meta_keyword=models.CharField(max_length=200,blank=True,verbose_name="Meta Keyword")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Cmspage, self).save(*args, **kwargs)

