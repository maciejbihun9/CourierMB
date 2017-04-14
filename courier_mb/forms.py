from django import forms

class SignUpForm(forms.Form):
    your_name_surname = forms.CharField(label= "", initial='Name & Surname', max_length=15)
    your_username = forms.CharField(label= "", initial='Username', max_length=10)
    email = forms.EmailField(label= "", initial='email', max_length=20)
    password = forms.CharField(label= "", initial='password', max_length=10, widget=forms.PasswordInput)
    repeat_password = forms.CharField(label= "", initial='repeat password', max_length=10, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('repeat_password')

        if password1 and password1 != password2:
            msg = "password does not match"
            self.add_error('repeat_password', msg)
            # raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data

class LoginForm(forms.Form):
    your_username = forms.CharField(label= "", initial='Username', max_length=10)
    password = forms.CharField(label= "", initial='password', max_length=10, widget=forms.PasswordInput)
    def clean(self):
        return super().clean()


class SenderForm(forms.Form):
    name_and_surname = forms.CharField(label="Your name and surname", initial='', max_length=20)
    company = forms.CharField(label="Company", initial='', max_length=20)
    country = forms.CharField(label="Country", initial='', max_length=20)
    address = forms.CharField(label="Address", initial='', max_length=20)
    postalCode = forms.CharField(label="Postal Code", initial='', max_length=20)
    city = forms.CharField(label="City", initial='', max_length=20)
    phone = forms.CharField(label="Phone", initial='', max_length=20)
    email = forms.EmailField(label="Email", initial='', max_length=20)

    def clean(self):
        cleaned_data = super().clean()
        address = cleaned_data.get("address")
        city = cleaned_data.get("city")
        if address == "":
            msg = "Provide valid address"
            self.add_error('valid_address', msg)
        if city == "":
            msg = "Provide valid city name"
            self.add_error('valid_address', msg)
        return cleaned_data


class ReceiverForm(forms.Form):
    name_and_surname = forms.CharField(label="Receiver name and surname", initial='', max_length=20)
    company = forms.CharField(label="Company", initial='', max_length=20)
    country = forms.CharField(label="Country", initial='', max_length=20)
    address = forms.CharField(label="Address", initial='', max_length=20)
    postalCode = forms.CharField(label="Postal Code", initial='', max_length=20)
    city = forms.CharField(label="City", initial='', max_length=20)
    phone = forms.CharField(label="Phone", initial='', max_length=20)
    email = forms.EmailField(label="Email", initial='', max_length=20)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data







