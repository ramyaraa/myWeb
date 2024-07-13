from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound


def january(request):
    return HttpResponse("in January eat apples") 

def february(request):
    return HttpResponse("in February eat bananas")

def monthly_challenge(request, month):
    if month == "january":
        text ="in January eat apples"
    elif month == "february":
        text ="in February eat bananas"
    elif month == "march":
        text ="in March eat oranges"
    elif month == "april":
        text ="in April eat pineapples"
    elif month == "may":
        text ="in May eat watermelons"
    else:
        return HttpResponseNotFound("Invalid month")
    return HttpResponse(text)

