from django.shortcuts import render
from .models import front , section1 , section2
# Create your views here.

def index(request):

   f = front.objects.all()
   sec1 = section1.objects.all()
   sec2 = section2.objects.all()



   return render(request, 'index.html', {"fr":f , "sec1":sec1 , "sec2":sec2} )
