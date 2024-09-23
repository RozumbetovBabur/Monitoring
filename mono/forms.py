from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class OfficeForm(forms.ModelForm):
    class Meta:
        model = office  # 'modal' emas, 'model' bo'lishi kerak
        fields = ('kobina', 'stol', 'turi')  # Maydonlar to'g'ri ko'rsatilgan
        widgets = {
            'kobina':forms.TextInput(attrs={'class':'form-control'}),
            'stol': forms.TextInput(attrs={'class': 'form-control'}),
            'turi': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SoupsFootForm(forms.ModelForm):
    class Meta:
        model = Soups_foot
        fields = "__all__"
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "lang": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }


class SaladsFootForm(forms.ModelForm):
    class Meta:
        model = Salads_foot
        fields = "__all__"
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "lang":forms.NumberInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
        }


class DishesToOrderForm(forms.ModelForm):
    class Meta:
        model = Dishes_to_order
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "lang": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }

class PizzaFootForm(forms.ModelForm):
    class Meta:
        model = Pizza_foot
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "lang": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }

class BeerForm(forms.ModelForm):
    class Meta:
        model = Breadbaza
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "lang": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }

class VnechniyFootForm(forms.ModelForm):
    class Meta:
        model = Vynechka_foot
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "lang": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }


class GrillFootForm(forms.ModelForm):
    class Meta:
        model = Giril_foot
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "lang": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }

class HomeFootForm(forms.ModelForm):
    class Meta:
        model = Home_foot
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "lang": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }

class TeaKarnaFootForm(forms.ModelForm):
    class Meta:
        model = Tea_Karna_foot
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "lang": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }


class ColdDrunksForm(forms.ModelForm):
    class Meta:
        model = Cold_drinks
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "lang": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }


class VodkaDrinksForm(forms.ModelForm):
    class Meta:
        model = Vodka_drinks
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "lang": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }

class PivoDrinksForm(forms.ModelForm):
    class Meta:
        model = Beer_drinks
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "lang": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }

class KnevaFootForm(forms.ModelForm):
    class Meta:
        model = Knivu_foot
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "lang": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }


class UserProfileForm(UserChangeForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=False,
        help_text="Оставьте поле пустым, если вы не хотите менять пароль."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Include other fields as needed
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])  # Update the password only if a new one is entered
        if commit:
            user.save()
        return user


class AdminProfileForm(UserChangeForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=False,
        help_text="Оставьте поле пустым, если вы не хотите менять пароль."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Include other fields as needed
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])  # Update the password only if a new one is entered
        if commit:
            user.save()
        return user