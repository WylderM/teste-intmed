from django.http import JsonResponse


def index_api(request):
    index = {
       "API":'Medicar V1',

   }
    return JsonResponse(index, safe=False)
