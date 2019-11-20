from django import forms
from .models import Student, Marks
from django.db import connection

class addform(forms.ModelForm):
	name = forms.CharField(max_length = 100)
	subject = forms.CharField(max_length = 100)
	roll_no = forms.IntegerField(min_value = 1)

	#optional
	marks = forms.FloatField()

	def save(self, commit=True):
		with connection.cursor() as c:
			c.execute("insert into app1_student values(%s, %s, %s)", (self.data['name'],self.data['subject'], int(self.data['roll_no'])))
			c.execute("insert into app1_marks values(%s,%s)",(int(self.data['roll_no']),float(self.data['marks'])))

	class Meta:
		model = Student
		fields = ['name', 'subject', 'roll_no']

class updateform(forms.Form):

	name = forms.CharField(max_length = 100 )
	subject = forms.CharField(max_length = 100)
	roll_no = forms.IntegerField(min_value = 1)

	#optional
	marks = forms.FloatField()

	def update(self):

		with connection.cursor() as c:
			c.execute("update app1_student set name=%s,subject=%s where roll_no=%s ", (self.data['name'],self.data['subject'], int(self.data['roll_no'])))
			c.execute("update app1_marks set marks=%s where roll_no=%s", ( float(self.data['marks']), int(self.data['roll_no'])))

	def save(self):
		pass

class deleteform(forms.Form):
	roll_no = forms.IntegerField(min_value=1)

	def doit(self):

		with connection.cursor() as c:
			c.execute("delete from app1_student where roll_no=%s",(int(self.data['roll_no']),))
			c.execute("delete from app1_marks where roll_no=%s",(int(self.data['roll_no']),))