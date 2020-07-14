from rest_framework import viewsets

from .serializer import studentSerializer
from .models import student

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = student.objects.all()
    serializer_class = studentSerializer
