from django.db import models

class Student(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


    # def __str__(self):
    #     # return self.name

class Task(models.Model):
    task_name= models.CharField(max_length=100)
    task_description= models.TextField()