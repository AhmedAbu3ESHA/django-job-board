from django.db import models

# Create your models here.
#from django field on website
JOBTYPE=(('FULL','FULL'),('PART','PART'))


class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class job(models.Model):

    titel=models.CharField(max_length =100)
    job_tybe=models.CharField(max_length=15 ,choices=JOBTYPE)
    description=models.TextField(max_length=1000)
    publishedat=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=0)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
#for return with titel after saving job
    def __str__(self):
         return self.titel

