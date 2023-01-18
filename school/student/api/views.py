
from student.models import Student,Class
from student.api.serializers import StudentSerializer,ClassSerializer
from rest_framework import viewsets

class Studentviewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    

class Classviewset(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer