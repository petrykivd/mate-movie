from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    remember_me = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }

    # def __init__(self, *args, **kwargs):
    #     super(RegisterForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'form-control'})
    #
    #     self.fields['first_name'].update({'placeholder': 'enter correct password'})
