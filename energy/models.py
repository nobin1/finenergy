from django.db import models
from django.contrib import admin

#class BlogPost(models.Model):
  #title = models.CharField(max_length=150)
  #body = models.TextField()
  #timestamp = models.DateTimeField()
  #def __unicode__(self):
	  #return self.title

#class Members(models.Model):
	#url = models.URLField(unique=True)
	#mtitle = models.CharField(max_length=200)
	#def __unicode__(self):
		#return self.mtitle
	
class Event(models.Model):
  ebody = models.TextField()
  etimestamp = models.DateTimeField()
  def __unicode__(self):
	  return self.ebody

#class BlogPostAdmin(admin.ModelAdmin):
#  list_display = ('title', 'timestamp')
  
#class MembersAdmin(admin.ModelAdmin):
#  list_display = ('mtitle',)
  
#class EventAdmin(admin.ModelAdmin):
#  list_display = ('ebody',)
  

#admin.site.register(BlogPost, BlogPostAdmin)
#admin.site.register(Members, MembersAdmin)
#admin.site.register(Event, EventAdmin)
