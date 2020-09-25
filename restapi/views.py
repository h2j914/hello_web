from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

# Create your views here.

# --1. --
def home(request):
    return HttpResponse("Hello, Django")

def taskstring(request):
    result = 'Rest API string!'
    return HttpResponse(result, content_type="text/plain")

# --2. JSON & XML--
def taskxml(request):
    result = '<employees><employee> \
              <firstName> John </firstName> <lastName> Doe </lastName> </employee> \
              <employee>  \
              <firstName>Anna</firstName> <lastName>Smith</lastName></employee> \
              </employees>'

    return HttpResponse(result, content_type='text/xml') # XML은 HTMl과 비슷 > HttpResponse 필요

def taskjson(request):
    result = {"employees":[
                           {"firstName":"John", "lastName":"Doe"},
                           {"firstName":"Anna", "lastName":"Smith"},
                           {"firstName":"Peter", "lastName":"Jones"}
                          ]
              }
    return JsonResponse(result) # JSON은 HttpResponse가 필요 없음, 대신 JsonResponse 필요