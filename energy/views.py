# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
#from energy.models import BlogPost
#from energy.models import Members
from energy.models import Event

#def archive(request):
  #posts = BlogPost.objects.all()
  #t = loader.get_template("archive.html")
  #c = Context({ 'posts': posts })
  #return HttpResponse(t.render(c))
  
  
#def members(request):
  #memberposts = Members.objects.all()
  #membert = loader.get_template("members.html")
  #memberc = Context({ 'mposts': memberposts })
  #return HttpResponse(membert.render(memberc))
  
def events(request):
  eposts = Event.objects.all()
  et = loader.get_template("events.html")
  ec = Context({ 'eposts': eposts })
  return HttpResponse(et.render(ec))
  

