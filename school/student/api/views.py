from student.models import Student,Class
from student.api.serializers import StudentSerializer,ClassSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class Studentviewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = serializer.data
        response['message'] = 'Student record successfully created.'
        headers = self.get_success_headers(serializer.data)
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        response = {
            'status': 'success',
            'message': 'Student successfully updated',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        student_id = self.kwargs.get('pk')
        student = Student.objects.get(id=student_id)
        # Perform custom delete logic
        is_deleted = student.delete()
        if is_deleted:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class Classviewset(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    
    def get_queryset(self):
        queryset = Class.objects.all()
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = serializer.data
        response['message'] = 'Class record successfully created.'
        headers = self.get_success_headers(serializer.data)
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        response = {
            'status': 'success',
            'message': 'Class successfully updated',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        Class_id = self.kwargs.get('pk')
        Class = Class.objects.get(id=Class_id)
        # Perform custom delete logic
        is_deleted = Class.delete()
        if is_deleted:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)