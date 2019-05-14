
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	#params={'name': 'Aniket ','place':'Indore'}
       # return HttpResponse('''<h1>Aniket</h1> <a href= "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">submit</a>''')
	return render(request,'index.html')
def about(request):
        return HttpResponse('''<h1>a+b=5</h1> <a href = "http://127.0.0.1:8000/index/">back</a>''')

#def removepunc(request):
#	djtext = request.GET.get('text','default')
#	print(djtext)
#	return HttpResponse("Remove punc")

def capfirst (request):
        djtext=request.POST.get('text','default')
        return HttpResponse("captalize first")

def newlineremove(request):
        djtext=request.POST.get('text','default')
        return HttpResponse("newline remover")

def spaceremove(request):
        djtext=request.POST.get('text','default')
        return HttpResponse("Space remover")
def charcount(request):
        djtext=request.GET.get('text','default')
        return HttpResponse("charcount")
def analyze(request):
	djtext = request.POST.get('text','default')
	removepunc = request.POST.get('removepunc','off')
	captalize = request.POST.get('captalize','off')
	newlineremover = request.POST.get('newlineremover','off')
	charcount= request.POST.get('charcount','off')
	extraspaceremover= request.POST.get('extraspaceremover','off')



        print(djtext)
	if removepunc=="on":
		punctuations='''!(){}[]?#@$%&*^~'":;/\_-'''
		analyze=""
		for char in djtext:
			if char not in punctuations:
				analyze= analyze+char
		params={'purpose':'Remove Punctuations','analyze_text':analyze}
		djtext=analyze
       # return ("Remove punc")
	#	return render(request,'analyze.html',params)
	if captalize =="on":
		analyze=""
		for char in djtext:
			analyze=analyze+char.upper()

		params={'purpose':'Upper case','analyze_text':analyze}
		djtext=analyze

	#	return render(request,'analyze.html',params)
       	if newlineremover =="on":
		analyze=""
                for char in djtext:
			if char !="\n":
                        	analyze=analyze+char.upper()

                params={'purpose':'Newline Remover','analyze_text':analyze}
		djtext=analyze
        #        return render(request,'analyze.html',params)
	if charcount =="on":
                analyze=""
		count=0;
                for char in djtext:
                        if char.isspace() !=True:
                                count=count+1
				analyze=count

                params={'purpose':'Newline Remover','analyze_text':analyze}
#		djtext=analyze
		return render(request,'analyze.html',params)
	if extraspaceremover =="on":
                analyze=""
                for index, char in enumerate(djtext):
                        if not (djtext[index]==" " and djtext[index+1]==" "):
                                analyze=analyze+char

                params={'purpose':'extraspaceRemover','analyze_text':analyze}
		djtext=analyze
       	return render(request,'analyze.html',params)


#	else:
#		return HttpResponse("Error")

def ex1(request):
	s='''<h1>Navigation bar</h1><br>
	<a href="https://www.youtube.com/watch?v=YZLKoG_vhDY">youtube<br>
	<a href="https://www.dezyre.com/article/top-10-machine-learning-algorith	ms/202">machine learning<br>'''
	return HttpResponse(s)
