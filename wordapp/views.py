from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .search import search, prioritizing 
import json


def search_view(request):
    return render(request, 'search_page.html', {})
	
	
def search_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get('term','')
        results = prioritizing(search(query.lower()), query.lower())
        data = json.dumps(results)
    else:
        data = 'fail'
    type = 'application/json'
    return HttpResponse(data, type)
	
	
def getSearchResults(request):
    if request.method == 'GET':
        query = request.GET.get('term') # for example: query = 'hello'
        if query:
            Result = prioritizing(search(query.lower()), query.lower())
            if len(Result) == 0:
                return JsonResponse({'Search_Result': "Word not found."})
            else:
                return JsonResponse({'Search_Result': Result})
        else:
            return redirect('/')