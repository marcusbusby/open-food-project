from django import forms
from userprofile.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('contributor', 'address')

class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()

		return user