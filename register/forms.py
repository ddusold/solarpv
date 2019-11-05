from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
    middle_name = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
    address = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))


class DashboardForm(forms.Form):
    client = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
    location = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
    product = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
    test_standard = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
    certificate = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-input'}))
