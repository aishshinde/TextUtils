# I have created this file- aish
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Chechbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover =request.POST.get('newlineremover', 'off')
    extraspaceremover =request.POST.get('extraspaceremover', 'off')
    charcounter =request.POST.get('charcounter', 'off')

    # Check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Removed Punctutions', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != "\r":
                analyzed += char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext=analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1]==' '):
                analyzed+=char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext=analyzed

    if charcounter == "on":
        analyzed = ''
        c=0
        for char in djtext:
            if char != ' ':
                c += 1
        analyzed = djtext+'\n'+str(c)
        params = {'purpose': 'Number of Characters', 'analyzed_text': analyzed}


    if charcounter != "on" and extraspaceremover != 'on' and newlineremover != "on" and fullcaps != 'on' and removepunc != 'on':
        return HttpResponse("Error")
    return render(request, 'analyze.html', params)
