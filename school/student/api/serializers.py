
from student.models import Student,Class
from rest_framework import serializers




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','age','class_name']
        
class ClassSerializer(serializers.ModelSerializer):
    classes = StudentSerializer(many=True)
    class Meta:
        model = Class
        fields = ['id','name','description','classes']