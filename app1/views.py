from django.shortcuts import render, redirect
from .models import Student, Marks
from .forms import *
from django.db import connection

def add(request):
	if request.method == 'POST':
		form = addform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('show')
	else:
		form = addform()
	return render(request, 'app1/add.html', {'form':form})

def show(request):
	students = Student.objects.raw('select * from app1_student')
	marks = Marks.objects.raw('select * from app1_marks')

	context = {
	'students' : students,
	'marks' : marks 
	}

	return render(request, 'app1/show.html', context)

def update(request):
	if request.method == 'POST':
		form = updateform(request.POST)
		if form.is_valid():
			form.update()

			return redirect('show')
	else:
		form = updateform()
	return render(request,'app1/update.html',{'form': form})

def delete(request):
	if(request.method == 'POST'):
		form = deleteform(request.POST)
		if form.is_valid():
			form.doit()

			return redirect('show')
	else:
		form = deleteform()
	return render(request,'app1/delete.html',{'form':form})


