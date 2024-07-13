from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse


month_dict = {
    "january": "in January eat apples",
    "february": "in February eat bananas",
    "march": "in March eat oranges",
    "april": "in April eat pineapples",
    "may": "in May eat mangos",
    "june": "in June eat watermelons",
    "july": "in July eat grapes",
    "august": "in August eat strawberries",
    "september": "in September eat blueberries",
    "october": "in October eat peaches",
    "november": "in November eat plums",
    "december": "in December eat dates",
}

def index(request):
    month_list= ""
    months = list(month_dict.keys())
    for month in months:
        cap_month = month.capitalize()
        month_path= reverse('monthly_challenge', args=[month])
        month_list += f"<li><a href='{month_path}'>{cap_month}</a></li>"

    response_data = f"<ul>{month_list}</ul>"
    return HttpResponse(response_data)
        
def monthly_challenge_by_number(request, month):
    months = list(month_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly_challenge", args=[redirect_month]) # create /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        text = month_dict[month]
        response_data = f"<h1>{text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Invalid month")

