from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from django.forms import ModelForm
from .models import UserProfile, Question


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return User





class EditUserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
        )

class EditProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        # fields = ['country', 'city', 'street', 'home', 'apartment', 'phone', 'zip']
        fields = '__all__'
        exclude = ['user']


class QuestionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name"
        self.fields['email'].label = "Email"
        self.fields['question'].label = "Ask your question"

    class Meta:
        model = Question
        fields = '__all__'
