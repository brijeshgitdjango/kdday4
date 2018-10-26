from django import forms
from .models import Student, SESSION_CHOICES,GENDER_CHOICES,YEAR_CHOICES,BRANCH_CHOICES




class StudentForm(forms.Form):
	name = forms.CharField(label="Name*",widget=forms.TextInput(attrs={'autofocus':'on', 'autocomplete':'off', 'class':'form-control', 'placeholder':'Name', "required":"required"}))
	rollno = forms.CharField(required=False,label="Roll No.", widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control', 'placeholder':'Roll No.'}))
	dob = forms.DateField(label="Date of birth*", widget=forms.SelectDateWidget(years=range(1990, 2010), attrs={'class':'form-control'}))
	gender = forms.CharField(label="Gender*", widget=forms.RadioSelect(choices=GENDER_CHOICES,attrs={'class':'form-sontrol'}))
	branch = forms.CharField(label="Branch*", widget=forms.Select(choices=BRANCH_CHOICES,attrs={'class':'form-sontrol'}))
	year = forms.CharField(label="Year*", widget=forms.Select(choices=YEAR_CHOICES,attrs={'class':'form-sontrol'}))
	session = forms.CharField(label="Session*", widget=forms.Select(choices=SESSION_CHOICES,attrs={'class':'form-sontrol'}))
	aadhar = forms.CharField(label="Aadhar", required=False, widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control', 'placeholder':'Aadhar No'}))
	mobile = forms.CharField(label="Mobile No.*", widget=forms.NumberInput(attrs={'autocomplete':'off','class':'form-control', 'placeholder':'Mobile No',"required":"required"}))
	fees_paid = forms.IntegerField(label="Fees paid*", widget=forms.NumberInput(attrs={'autocomplete':'off','class':'form-control', 'placeholder':'Fees paid',"required":"required"}))
	address = forms.CharField(label="Address*",widget=forms.TextInput(attrs={'autocomplete':'off', 'class':'form-control', 'placeholder':'Address',"required":"required"}))
	email = forms.EmailField(label="Email",required=False,widget=forms.EmailInput(attrs={'autocomplete':'off', 'class':'form-control', 'placeholder':'Email'}))
	roomno = forms.CharField(label='Room No.*', widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control',"required":"required"}))

	def clean_mobile(self):
		mobile = self.cleaned_data.get('mobile')
		if len(mobile)!=10:
			raise forms.ValidationError('Incorrect mobile Number')
		return mobile

	class Meta:
		model=Student
		fields=['name'

			'rollno',
			'dob',
			'branch',
			'session',
			'gender',
			'aadhar',
			'mobile',
			'fees_paid',
			'address',
			'email',
			'year',
			'roomno',

		]

