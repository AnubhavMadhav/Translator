from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator


# Create your views here.

def home(request):
    return render(request, "translate/index.html")

def result(request):
    
    
    text = request.POST.get('text')
    
    translator = Translator()
    
    result = translator.translate(text, dest='hi')
    
    
    return HttpResponse(result.text)