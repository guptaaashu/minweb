from django.db import models
from accounts.models import *

Typelist = (
    ('0', 'Internship'),
    ('1', 'Job'),
    ('2', 'Project',)
)
Field= (
  ('0', 'Django'),
    ('1', 'PHP'),
    ('2', 'Android',)
)
Year= (
  ('0','1'),
    ('1', '2'),
    ('2', '3',)
)

class Alumni(models.Model):
    user = models.ManyToManyField(MyUser,blank=True)
    name=models.CharField(max_length=200)
    field = models.CharField(max_length=200,choices = Field,null=True,blank=True)
    year = models.CharField(max_length=200,choices = Year,null=True,blank=True)
    typelist = models.CharField(max_length=200,choices = Typelist,null=True,blank=True)
    name = models.CharField(max_length=200)
    start = models.DateField(blank=True,null=True,db_index=True)
    end = models.DateField(blank=True,db_index=True,null=True)
    detail=models.TextField(null=True,blank=True)
    photo = models.ImageField(upload_to="images/", blank=True,null=False)
    department= models.CharField(max_length=200)
    def __str__(self):          
        return self.name
    
