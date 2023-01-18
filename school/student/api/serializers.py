
from student.models import Student,Class
from rest_framework import serializers




class StudentSerializer(serializers.ModelSerializer):
    class_name = serializers.CharField(source='class_id.name')

    class Meta:
        model = Student
        fields = ['id','name','age','class_name']
        
class ClassSerializer(serializers.ModelSerializer):
    stu = StudentSerializer(many=True,read_only=True)
    class Meta:
        model = Class
        fields = ['id','name','description','stu']