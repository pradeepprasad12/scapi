from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    
    def __str__(self):
        return self.name

  
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    class_id = models.ForeignKey(Class,on_delete=models.CASCADE,related_name='stu',null=True,blank=True)

    def __str__(self):
        return self.name
  

