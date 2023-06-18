from django.shortcuts import render
from .models import job
# Create your views here.

def job_list(request):
    joblist=job.objects.all()
    context={'jobs':joblist}
    return render(request,'jobs/job_list.html',context)

def job_des(request,id):
    jobdes=job.objects.get(id=id)
    context={'job':jobdes}
    return render(request,'jobs/job_des.html',context)
