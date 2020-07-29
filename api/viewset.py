from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import studentSerializer
from .models import student
from django.shortcuts import get_object_or_404
from rfw.celery import *
from rest_framework.decorators import action



class StudentViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = student.objects.all()
    serializer_class = studentSerializer

    
    @action(detail=False)
    # @action(detail=True,methods=["GET"])
    def  task(self,request):

        debug_task.delay()
        return Response({"task":"under progress"})


    def list(self, request):
      
        
        queryset = student.objects.all()
        # print(queryset,"hiiii")
        serializer = studentSerializer(queryset, many=True)
        # print(Response(serializer.data),"hiiii")
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = student.objects.all()
        students = get_object_or_404(queryset, pk=pk)
        # print(queryset[0].name,"hiiii")
        
        serializer = studentSerializer(students)
        return Response(serializer.data)
        

