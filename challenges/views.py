from django.shortcuts import render
from django.http import HttpResponse


def january(request):
    return HttpResponse("in January eat apples") 

def february(request):
    return HttpResponse("in February eat bananas")

