from django import forms
from django.contrib.auth.models import User

from .models import Application


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Create a password",
            }
        ),
        min_length=8,
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Confirm your password",
            }
        )
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Your first name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Your last name",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Choose a username",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "you@example.com",
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data["email"].lower().strip()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "An account with this email already exists."
            )

        return email

    def clean_username(self):
        username = self.cleaned_data["username"].strip()

        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                "This username is already taken."
            )

        return username

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error(
                "confirm_password",
                "Passwords do not match."
            )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data["password"])
        user.is_staff = False

        if commit:
            user.save()

        return user
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["cv", "cover_letter"]

        widgets = {
            "cv": forms.ClearableFileInput(
                attrs={
                    "class": "form-input",
                    "accept": ".pdf,.doc,.docx",
                }
            ),
            "cover_letter": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "placeholder": "Tell the hiring team why you're a good fit...",
                    "rows": 7,
                }
            ),
        }

    def clean_cv(self):
        cv = self.cleaned_data.get("cv")

        if not cv:
            raise forms.ValidationError(
                "Please upload your CV."
            )

        allowed_extensions = [".pdf", ".doc", ".docx"]

        extension = cv.name.lower().rsplit(".", 1)[-1]

        if f".{extension}" not in allowed_extensions:
            raise forms.ValidationError(
                "Only PDF, DOC or DOCX files are allowed."
            )

        if cv.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "CV file size must be 5 MB or less."
            )

        return cv    