from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
class Article(models.Model):
    title 			= models.CharField(max_length=120, blank=False)
    #tags			= models.CharField(max_length=120, default='tag1')
    tags			= TaggableManager()
    category		= models.CharField(max_length=120, blank=True)
    data_created    	= models.DateTimeField(default=timezone.now)
    last_modified   	= models.DateTimeField(default=timezone.now)
    author 			= models.CharField(max_length=120, default='admin') #text			= MDTextField()
    description       	= models.TextField(blank=False, null=True)	
    text            	= models.TextField(blank=False, null=True)	
#	text            	= MarkdownxField()	

    def get_absolute_url(self):
        return reverse ("article-detail", kwargs= {"pk":self.id})
    
    def get_update_url(self):
        return reverse ("article-update", kwargs= {"pk":self.id})
    
    def get_delete_url(self):
        return reverse ("article-delete", kwargs= {"pk":self.id})
