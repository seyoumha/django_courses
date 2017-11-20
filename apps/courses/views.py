from django.shortcuts import render, HttpResponse, redirect
from models import Course, Description
from django.contrib import messages

def index(request):
    return render(request, 'courses/index.html', {'courses': Course.objects.all(), 'desc': Description.objects.all()})
def create(request):
    errors = Course.objects.basic_validator(request.POST)
    desc_errors = Description.objects.basic_validator(request.POST)
    print desc_errors
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    if len(desc_errors):
        for tag, error in desc_errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect ('/')
    else:
        course = Course.objects.create(name=request.POST['name'])
        Description.objects.create(desc=request.POST['desc'], course_id = course.id)
        return redirect('/')
def destroy(request,id):
    context={
    'course': Course.objects.get(id=id)
    }
    return render(request,'courses/destroy.html', context)
def delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')