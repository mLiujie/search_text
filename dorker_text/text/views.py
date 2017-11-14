from django.shortcuts import render,render_to_response
from django.http import HttpResponse
# Create your views here.

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
	html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
    return HttpResponse('<table>%s</table>'% '\n'.join(html))

def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if "q" in request.GET:
	message = 'you searched for:%r'% request.GET['q']
    else:
	message = 'you submitted an empty form'
    return HttpResponse(message)
'''
def search_html():
    if "q"in request.GET:
	message = 'you searched for :%r'% request.GET['q']
    else:	
	message = 'you submitted an empty form'
    return HttpResponst(message)

'''
