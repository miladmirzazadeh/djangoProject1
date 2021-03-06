from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
def response(request):
    template = loader.get_template('blog/login2.html')
    content = template.render(context={}, request=request)
    return(HttpResponse(content))