from django.shortcuts import render
from django.http import HttpResponse
from hello_app.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    #return HttpResponse("Hello World!")
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict={"access_records":webpages_list} 
    #my_dict = {'insert_me':"Hello  I am from  first app and views.py!"}
    return render(request, 'first_app\\index.html', context=date_dict)
    
#this is case sensitive, so be careful
#return render(request, "index.html", context=my_dict)
    
