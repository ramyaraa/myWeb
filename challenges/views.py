from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect


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
# def monthly_challenge_by_number(request, month):
#     months = {
#         1: "january",
#         2: "february",
#         3: "march",
#         4: "april",
#         5: "may",
#         6: "june",
#         7: "july",
#         8: "august",
#         9: "september",
#         10: "october",
#         11: "november",
#         12: "december",
#     }
#     if month in months:
#         redirect_month = months[month]
#         #redirect it means redirect to another page forexample you type 3 it will redirect you to march
#         return HttpResponseRedirect(redirect_month)
#     else:
#         return HttpResponseNotFound("Invalid month")

def monthly_challenge_by_number(request, month):
    months = list(month_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    # you can use this
    # return HttpResponseRedirect(redirect_month)
    # or this     it is same thing
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        text = month_dict[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Invalid month")

