# i have created this file -- saurabh patel
from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')

    #checkbox value
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    Removenewline = request.GET.get('newlineremover', 'off')
    Removeextraspace = request.GET.get('Extraspaceremover', 'off')
    countcharacter = request.GET.get('charactercounter', 'off')
   #check which checkbox is on
    if removepunc == "on":
       punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
       analyzed = ""
       for char in djtext:
           if char not in punctuations:
              analyzed += char
       params = {'purpose': 'Removed Punctutations', 'analyzed_text': analyzed}

       return render(request, 'analyze.html', params)
    elif(fullcaps=="on"):
        analyzed=""
        analyzed+=djtext.upper()
    elif(Removenewline=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed += char
        params = {'purpose': 'Removed newlines', 'analyzed_text': analyzed}
    elif(Removeextraspace=="on"):
        analyzed = ""
        for index,char in enumerate (djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                     analyzed += char
        params = {'purpose': 'Removed newlines', 'analyzed_text': analyzed}
    elif(countcharacter=="on"):
        analyzed=""
        count=0
        for char in djtext:
            if char!=" ":
                count=count+1
        params = {'purpose': 'Removed newlines', 'analyzed_text': analyzed}
    else:
        return HttpResponse("Please check the box")

# def capfirst(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='http://127.0.0.1:8000/'>back</a>")
# def charcount(request):
#     return HttpResponse("charcount")
