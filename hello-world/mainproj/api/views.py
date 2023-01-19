from django.http import JsonResponse

def GetRoutes(request):
    routes = [
        {'GET': '/api/projects'},
        {'POST': '/api/projects'}
    ]

    return JsonResponse(routes, safe=False)