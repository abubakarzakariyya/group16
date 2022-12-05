from django.db import models
class fire_service(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length= 255)
    
    fire_degree_categories=[
        ('1st degree','1ST DEGREE'),
        ('2nd degree','2ND DEGREE'),
        ('3rd degree','3RD DEGREE')
    ]
    
    fire_degree=models.CharField(max_length = 11, choices = fire_degree_categories)
    
    fire_dept_categories = [
        ('class a','CLASS A'),
        ('class b','CLASS B'),
        ('class c','CLASS C'),
        ('class d','CLASS D'),
        ('class e','CLASS E')
        
    ]
    fire_departments = models.CharField(max_length = 10, choices = fire_dept_categories)
    No_of_tanks = models.PositiveIntegerField()
    water_hoses = models.PositiveIntegerField()
    comments = models.TextField()
    date_time_started = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    