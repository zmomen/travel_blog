from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # define the metadata for the class I am in.
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  )

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()
            return user


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:20%'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:20%'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:20%'}))

    class Meta:
        model = User
        fields = ('email',
                  'first_name',
                  'last_name',
                  'password',
                  )
#        exclude()
