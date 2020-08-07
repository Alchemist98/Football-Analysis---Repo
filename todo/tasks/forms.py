#form represenatation of models
#we've this model task when we speicfy which model its gonna replicate it creates all the form fields for us

from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
	task = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = Task
		fields = '__all__'
			
