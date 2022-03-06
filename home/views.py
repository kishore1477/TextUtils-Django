import string
import re 
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from collections import Counter
 
# Create your views here.
def index(request):
    params = {"name": 'Kishore'}
    return render(request, 'index.html', params)
def  contact(request):
    params = {"name": 'Kishore'}
    return render(request, 'contact.html', params)
    # return HttpResponse("Welcome to home page")

def analyze(request):
    
        # get the text
    djtext =  request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    captilizefirst = request.POST.get('captilizefirst', 'off')
    removespaces = request.POST.get('removespaces', 'off')
    capatilizefleter  = request.POST.get('capatilizefleter', 'off')
    upper  = request.POST.get('upper', 'off')
    lower  = request.POST.get('lower', 'off')
    wordcounter   = request.POST.get('wordcounter', 'off')
    charactercounter    = request.POST.get('charactercounter', 'off')
    newlineremover    = request.POST.get('newlineremover', 'off')
    djtext_length = len(djtext)
    array =[removepunc,captilizefirst,removespaces,capatilizefleter,upper,lower,wordcounter,charactercounter]
    # print(array[1])
    # for char in array:
    #     if( (array[char]=="on")):
    #         return HttpResponse("Please check on at a time!")
    #         # if(char >1)
    # if (removepunc == "on" and captilizefirst  == "on" and   removespaces == "on"):
    #        return HttpResponse("Please check one at a time!")
   
                           
    if (djtext_length > 0):
      
            if      lower == "on":
                            djtext = djtext.lower()  
                            
                            analyzed =  djtext
                            params = {'purpose': 'Lower Case'+ "("+     lower + ")", 'analyzed_text': analyzed}
                            djtext = analyzed
                            # return render(request, 'analyze.html', params)
            if (    upper == "on"):
                            analyzed=""
                            for char in djtext:
                                analyzed=analyzed+char.upper()
                            params = {'purpose': 'Upper Case'+ "("+    upper + ")", 'analyzed_text': analyzed}
                            # return render(request, 'analyze.html', params)
                            djtext = analyzed
            if(    capatilizefleter == "on"):
                
                            djtext2 = djtext.lstrip() 
                            djtext = djtext2.capitalize() 
                            
                            analyzed =  djtext
                            params = {'purpose': 'Capatilize first only letter'+ "("+   capatilizefleter + ")", 'analyzed_text': analyzed}
                            # return render(request, 'analyze.html', params)
                            djtext = analyzed
            
            if (  removespaces == "on"):
                            # djtext1 = djtext.strip() 
                            # djtext1 = djtext.replace(" ")  
                            # analyzed = re.sub('\s+','',  djtext)
                            # analyzed = ""
                            # for char in djtext :
                            #     if " " not in char:
                            #        analyzed =  analyzed + char
                            analyzed = ""
                            for index, char in enumerate(djtext):
                                     if not(djtext[index] == " " and djtext[index+1]==" "):
                                          analyzed = analyzed + char

                            # analyzed = djtext1
                            params = {'purpose': 'Remove Spaces'+ "("+  captilizefirst + ")", 'analyzed_text': analyzed}
                            # return render(request, 'analyze.html', params)
                            djtext = analyzed
            
            if(  captilizefirst == "on"):
                            djtext = djtext.title() 
                            
                            analyzed =  djtext
                            params = {'purpose': 'capatilize first leter'+ "("+  captilizefirst + ")", 'analyzed_text': analyzed}
                            # return render(request, 'analyze.html', params)
                            djtext = analyzed 
            if newlineremover=="on":
                            analyzed=""
                            for char in djtext:
                                if char!="\n":
                                    analyzed=analyzed+char
                            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    # Analyze the text

                            # return render(request, 'analyze.html', params)
                            djtext = analyzed 
            if( removepunc == "on"):
                            punctuations =  string.punctuation
                            punc = punctuations
                            print(punc)
                            analyzed = ""
                            for char in djtext:
                                if char not in punctuations:
                                    analyzed = analyzed + char
                            params = {'purpose': 'Removed Punctuations'+ "("+ removepunc + ")", 'analyzed_text': analyzed}
                            # return render(request, 'analyze.html', params)
                            djtext = analyzed 
            if(  wordcounter == "on"):
                            djtext2= djtext.split()
                            words =len(djtext2) 
                            analyzed = words
                            
                            params = {'purpose': 'Word count'+ "("+wordcounter   + ")", 'analyzed_text': analyzed}
                            # return render(request, 'analyze.html', params)
                            djtext = analyzed 
            if(   charactercounter == "on"):
                        
                            count = 0
                            for i in  djtext:
                                
                                if( i != " "   and  i != "\n"):
                                   count = count + 1
                            # djtext2= djtext.split()
                            # djtext2= djtext 
                            # letters =  Counter(djtext)
                            # for char in djtext:
                            #     print(char)
                            #     # words =len(char) -  char.count(" ")
                            
                            
                            analyzed =   count
                            
                            params = {'purpose': ' Character count'+ "("+ charactercounter  + ")", 'analyzed_text': analyzed}
                            # return render(request, 'analyze.html', params)
            if(removepunc !="on" and   removespaces !="on" and   captilizefirst !="on" and capatilizefleter !="on" and upper!="on" and lower !="on" and wordcounter !="on" and charactercounter != "on" and newlineremover != "on"):
                  params = {'purpose': 'failed'+ "("+ "Error"   + ")", 'analyzed_text':  'Please check any option for analyzing your text .'}   
                  return render(request, 'analyze.html', params)
                            # return HttpResponse("Please check any option for analyzing your text .")                
            
             
            # params = {'purpose': 'failed'+ "("+wordcounter   + ")", 'analyzed_text':  'check some error occured'}   
             #  return render(request, 'analyze.html', params)
            return render(request, 'analyze.html', params) 
    else:
       params = {'purpose': 'failed'+ "("+ "Error"   + ")", 'analyzed_text':  'Enter something  for analyzing'}   
    return render(request, 'analyze.html', params)
                              
            
        
           
        # else:
        #     return HttpResponse('Error : Please Enter Something.')
       
                                                            

# def  removepunc(request):
#     # get the text
#    djtext =  request.GET.get('text', 'default')
#    print(djtext)
   
#    return HttpResponse("Welcome to  removepunc page")
# def   capatilizefirst(request):
#     return HttpResponse("Welcome to   capatilizefirst page")
# def   newlineremove(request):
#     return HttpResponse("Welcome to   newlineremove page")
# def   spaceremove(request):
#     return HttpResponse("Welcome to   spaceremove page <a href = '/'> back </a>")
# def    charcount(request):
#     return HttpResponse("Welcome to    charcount page")