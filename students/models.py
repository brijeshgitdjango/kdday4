from django.db import models

SESSION_CHOICES = (
	('2017-18','2017-18'),
	('2018-19','2018-19'),
	('2019-20','2019-20'),
	)

GENDER_CHOICES = (('Male','Male'), ('Female','Female'))
YEAR_CHOICES = (
	(1,'First'), 
	(2,'Second'),
	(3,'Third'),
	(4,'Fourth'),
	)

BRANCH_CHOICES = (
	('Computer Science and Engineering','Computer Science and Engineering'),
	('Electronics and Communication Engineering','Electronics and Communication Engineering'),
	('Mechanical Engineering','Mechanical Engineering'),
	('Aeronautical Engineering','Aeronautical Engineering'),
	)

class Student(models.Model):

	name = models.CharField(max_length=50)
	rollno = models.CharField(max_length=10,null=True, blank=True)
	dob = models.DateField()
	branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
	session = models.CharField(max_length=7, choices=SESSION_CHOICES, default="2018-19")
	gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="Male")
	aadhar = models.CharField(max_length=12, null=True, blank=True)
	mobile = models.CharField(max_length=10,unique=True)
	fees_paid = models.IntegerField()
	pending_fees = models.IntegerField(null=True, blank=True)
	fully_paid = models.BooleanField(default=False)
	address = models.CharField(max_length=200)
	email = models.EmailField(null=True, blank=True)
	year = models.IntegerField(choices=YEAR_CHOICES, default=1)
	roomno = models.CharField(max_length=5,null=True, blank=True)
	bedno = models.CharField(max_length=1,null=True, blank=True)
	timestamp = models.DateField(auto_now=False,auto_now_add=True)
	updated = models.DateField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["name"]