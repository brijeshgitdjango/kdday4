from django import forms
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from room.models import Room, Bed
from .forms import StudentForm
from .models import Student


def StudentRegisterView(request):
	form = StudentForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			name = form.cleaned_data.get('name')
			rollno = form.cleaned_data.get('rollno')
			session = form.cleaned_data.get('session')
			dob = form.cleaned_data.get('dob')
			branch = form.cleaned_data.get('branch')
			gender = form.cleaned_data.get('gender')
			aadhar = form.cleaned_data.get('aadhar')
			mobile = form.cleaned_data.get('mobile')
			fees_paid = form.cleaned_data.get('fees_paid')
			address = form.cleaned_data.get('address')
			email = form.cleaned_data.get('email')
			year = form.cleaned_data.get('year')
			roomno = form.cleaned_data.get('roomno')
			bedno = None
			fully_paid = None

			if len(Student.objects.filter(mobile=mobile)):
				context = {
					'form':form,
					'rooms':Room.objects.filter(fully_allocated=False),
					'msg':"Mobile already registered"
				}
				return render(request, 'student/student_register.html', context)


			if fees_paid>=40000:
				fully_paid=True
			else:
				fully_paid=False
			room_obj = get_object_or_404(Room, roomno=int(roomno))
			bed_obj = get_object_or_404(Bed, room=room_obj)
			count = bed_obj.allocated_count
			if not bed_obj.A:
				bedno = 'A'
				bed_obj.A=True
				bed_obj.a_allocated_to=mobile
				count += 1
			elif not bed_obj.B:
				bedno = 'B'
				bed_obj.B=True
				bed_obj.b_allocated_to=mobile
				count += 1
			elif not bed_obj.C:
				bedno = 'C'
				bed_obj.C=True
				bed_obj.c_allocated_to=mobile
				count += 1
			else:
				bedno = 'D'
				bed_obj.D=True
				bed_obj.d_allocated_to=mobile
				count += 1
			if count==4:
				fully_allocated=True
			else:
				fully_allocated=False
			room_obj.fully_allocated = fully_allocated
			room_obj.save()
			bed_obj.allocated_count = count
			bed_obj.save()
			obj = Student(
					name=name,
					rollno=rollno,
					dob=dob,
					session=session,
					branch=branch,
					gender=gender,
					aadhar=aadhar,
					mobile=mobile,
					fees_paid=fees_paid,
					address=address,
					email=email,
					year=year,
					roomno=roomno,
					bedno=bedno,
					fully_paid=fully_paid,
					pending_fees=40000-fees_paid
				)
			obj.save()
			return HttpResponseRedirect(reverse("students:list"))
	context = {
		'form':form,
		'rooms':Room.objects.filter(fully_allocated=False) 
	}
	return render(request, 'student/student_register.html', context)


def StudentListView(request):
    obj_list = Student.objects.all()
    context = {
		'obj_list':obj_list,
		'title':'Students List(All)'
	}
    return render(request, 'student/students_list.html', context)


def StudentPendingView(request):
	obj_list = Student.objects.filter(fully_paid=False)
	context = {
		'obj_list':obj_list,
		'title':'Students List(Pending Fees)'
	}
	return render(request, 'student/students_list.html', context)


def StudentDetailView(request, id=None):
	instance = get_object_or_404(Student, id=id)
	context = {
		'instance':instance,
	}
	return render(request, 'student/students_detail.html', context)

def StudentUpdateView(request, id=None):
	instance = get_object_or_404(Student, id=id)
	initial_data = {
		"name":instance.name,
		"session":instance.session,
		'rollno':instance.rollno,
		'dob':instance.dob,
		'branch':instance.branch,
		'gender':instance.gender,
		'aadhar':instance.aadhar,
		'mobile':instance.mobile,
		'fees_paid':instance.fees_paid,
		'email':instance.email,
		'year':instance.year,
		'roomno':instance.roomno,
		'bedno':instance.bedno,
		'address':instance.address,

	}
	form = StudentForm(request.POST or None, initial=initial_data)
	if request.method=="POST":
		if form.is_valid():
			instance = get_object_or_404(Student, id=id)
			name = form.cleaned_data.get('name')
			rollno = form.cleaned_data.get('rollno')
			session = form.cleaned_data.get('session')
			dob = form.cleaned_data.get('dob')
			branch = form.cleaned_data.get('branch')
			gender = form.cleaned_data.get('gender')
			aadhar = form.cleaned_data.get('aadhar')
			mobile = form.cleaned_data.get('mobile')
			fees_paid = form.cleaned_data.get('fees_paid')
			address = form.cleaned_data.get('address')
			email = form.cleaned_data.get('email')
			year = form.cleaned_data.get('year')
			roomno = form.cleaned_data.get('roomno')
			bedno = form.cleaned_data.get('bedno')

			if instance.mobile!=mobile and len(Student.objects.filter(mobile=mobile)):
				context = {
					'form':form,
					'rooms':Room.objects.filter(fully_allocated=False),
					'msg':"Mobile already registered"
				}
				return render(request, 'student/student_register.html', context)
			
			if fees_paid>=40000:
				fully_paid=True
			else:
				fully_paid=False

			
			instance.name=name
			instance.rollno=rollno
			instance.dob=dob
			instance.branch=branch
			instance.gender=gender
			instance.aadhar=aadhar
			instance.mobile=mobile
			instance.fees_paid=fees_paid
			instance.address=address
			instance.email=email
			instance.year=year
			instance.fully_paid=fully_paid
			instance.pending_fees=40000-fees_paid

			if instance.roomno==roomno:
				instance.roomno=instance.roomno
				instance.bedno=instance.bedno

			else:
				# deallocating previous seat
				if instance.roomno:
					room_obj = get_object_or_404(Room, roomno=int(instance.roomno))
					bed_obj = get_object_or_404(Bed, room=room_obj)
					bedno_ = instance.bedno

					if bedno_=="A":
						bed_obj.A=False
						bed_obj.a_allocated_to=None
					elif bedno_=="B":
						bed_obj.B=False
						bed_obj.b_allocated_to=None
					elif bedno_=="C":
						bed_obj.C=False
						bed_obj.c_allocated_to=None
					else:
						bed_obj.D=False
						bed_obj.d_allocated_to=None

					bed_obj.allocated_count = bed_obj.allocated_count-1
					bed_obj.save()
					room_obj.fully_allocated=False
					room_obj.save()

				# allocating new seat
				room_obj = get_object_or_404(Room, roomno=int(roomno))
				bed_obj = get_object_or_404(Bed, room=room_obj)
				count = bed_obj.allocated_count

				if not bed_obj.A:
					bedno = 'A'
					bed_obj.A=True
					bed_obj.a_allocated_to=mobile
					count += 1
				elif not bed_obj.B:
					bedno = 'B'
					bed_obj.B=True
					bed_obj.b_allocated_to=mobile
					count += 1
				elif not bed_obj.C:
					bedno = 'C'
					bed_obj.C=True
					bed_obj.c_allocated_to=mobile
					count += 1
				else:
					bedno = 'D'
					bed_obj.D=True
					bed_obj.d_allocated_to=mobile
					count += 1

				if count==4:
					fully_allocated=True
				else:
					fully_allocated=False

				room_obj.fully_allocated = fully_allocated


				room_obj.save()

		
				bed_obj.allocated_count = count

				bed_obj.save()

				instance.roomno=roomno
				instance.bedno=bedno
				

			instance.save()
			return HttpResponseRedirect(reverse("students:list"))
	context = {
		'form':form,
		'rooms':Room.objects.filter(fully_allocated=False),
		'form_update':True,
		'roomno':instance.roomno,
	}
	return render(request, 'student/student_register.html', context)


def StudentDeleteView(request, id=None):
	instance = get_object_or_404(Student, id=id)
	if request.method=="POST":

		room_obj = get_object_or_404(Room, roomno=int(instance.roomno))
		bed_obj = get_object_or_404(Bed, room=room_obj)
		bedno_ = instance.bedno

		if bedno_=="A":
			bed_obj.A=False
			bed_obj.a_allocated_to=None
		elif bedno_=="B":
			bed_obj.B=False
			bed_obj.b_allocated_to=None
		elif bedno_=="C":
			bed_obj.C=False
			bed_obj.c_allocated_to=None
		else:
			bed_obj.D=False
			bed_obj.d_allocated_to=None

		bed_obj.allocated_count = bed_obj.allocated_count-1
		bed_obj.save()
		room_obj.fully_allocated=False
		room_obj.save()

		instance.delete()
		return HttpResponseRedirect(reverse("students:list"))
	context = {
		'instance':instance,
	}

	return render(request, 'student/student_delete.html', context)


def StudentSearchView(request):
	if request.method=='POST':
		mobile = request.POST.get('mobile')
		instance = Student.objects.filter(mobile=mobile)
		if len(instance):
			
			return HttpResponseRedirect(reverse('students:detail', kwargs={'id':instance.first().id}))
		else:
			return render(request, 'student/students_detail_no.html',{})
	else:
		return HttpResponseRedirect(reverse('students:list'))
