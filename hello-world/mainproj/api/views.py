from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from firstapp.models import FirstApp
from .serializers import FirstAppSerializer

@api_view(['GET'])
def GetRoutes(request):
    routes = [
        {'GET': '/api/projects/'},
        {'GET': '/api/projects/<str:id>/'},
        {'POST': '/api/projects/'}
    ]
    return Response(routes)

@api_view(['GET'])
def GetProjects(request):
    projects = FirstApp.objects.all()
    serializer = FirstAppSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetProject(request, pk):
    projects = FirstApp.objects.get(id=pk)
    serializer = FirstAppSerializer(projects, many=False)
    return Response(serializer.data)