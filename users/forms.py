from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import NaturalDonor, Beneficiary, User, Institution, LegalDonor, Admin


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su correo electrónico'
    }))

    TI = 1
    CC = 2
    CE = 3
    NIT = 4

    id_type_choices = [(TI, 'Tarjeta de Identidad'),
                       (CC, 'Cédula de Ciudadanía'),
                       (CE, 'Cédula extranjera'),
                       (NIT, 'NIT')]

    idType = forms.ChoiceField(label='Tipo de identificación', widget=forms.Select(attrs={
        'class': 'form-control'
    }), choices=id_type_choices)
    numID = forms.CharField(label='Número de identificación', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su número de identificación'
    }))

    profilePicture = forms.ImageField(label='Foto de perfil', widget=forms.FileInput(attrs={
        'class': 'form-control'
    }), required=False)

    password1 = forms.CharField(label='Contraseña', strip=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Crea una contraseña',
        'autocomplete': 'current-password',
    }))

    password2 = forms.CharField(label='Confirmación de contraseña', strip=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirma tu contraseña',
        'autocomplete': 'current-password',
    }))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['profilePicture'].initial = 'users/profile_default.png'

        self.fields['idType'].choices = [
            choice for choice in self.id_type_choices if choice[0] != User.NIT
        ]

        if self.instance:
            if isinstance(self.instance, Institution) or isinstance(self.instance, LegalDonor):
                self.fields['idType'].choices = [
                    (User.NIT, 'NIT')
                ]
                self.fields['name'] = forms.CharField(label='Razón Social', widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la razón social'
                }))
            else:
                self.fields['name'] = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre'
                }))

        if self.instance:
            if isinstance(self.instance, NaturalDonor):
                role = forms.CharField(widget=forms.HiddenInput(), initial=User.NATURALDONOR)
        
        if self.instance:
            if isinstance(self.instance, Admin):
                self.fields['idType'].choices = [
                    (User.CC, 'Cédula de Ciudadanía'),
                    (User.CE, 'Cédula extranjera')
                ]




    class Meta:
        model = NaturalDonor
        fields = ("name", "email", "password1", "password2", "idType", 'numID', 'profilePicture')
        labels = {
            "name": "Nombre",
            "email": "Correo electrónico",
            "idType": "Tipo de identificación",
            "numID": "Número de identificación",
            "profilePicture": "Foto de perfíl"
        }


class CustomUserCreationBenForm(CustomUserCreationForm):
    birth_date = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su fecha de nacimiento',
        'type': 'date',
    }))
    optionsGender = (('F', 'Femenino'),
                     ('M', 'Masculino'),
                     ('O', 'Otro'))

    gender = forms.ChoiceField(label='Genero', widget=forms.Select(attrs={
        'class': 'form-control'
    }), choices=optionsGender)

    role = forms.CharField(widget=forms.HiddenInput(), initial=User.BENEFICIARY)

    class Meta:
        model = Beneficiary
        fields = ("name", "email", "password1", "password2", "idType", 'numID', 'profilePicture', 'gender',
                  'birth_date')


class LegalDonorForm(CustomUserCreationForm):
    organization_type_choices = (
        ('foundation', 'Fundación o Beca'),
        ('company', 'Empresa o Empleador'),
        ('alumni_association', 'Asociación de Exalumnos'),
        ('charity', 'Organización Benéfica o Sin Fines de Lucro'),
        ('community_organization', 'Organización Comunitaria'),
        ('mentoring_program', 'Programa de Tutoría o Mentoría'),
        ('religious_organization', 'Organización Religiosa'),
        ('government', 'Gobierno u Organismo Público'),
    )

    organization_type = forms.ChoiceField(
        label='Tipo de Organización',
        choices=organization_type_choices,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    description = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
        })
    )

    role = forms.CharField(widget=forms.HiddenInput(), initial=User.LEGALDONOR)
    class Meta:
        model = LegalDonor
        fields = ("name", "email", "password1", "password2", "idType", 'numID', 'profilePicture',
                  "organization_type", "description")


class CustomInstitutionForm(CustomUserCreationForm):
    type_institution = forms.MultipleChoiceField(
        choices=Institution.TYPE_CHOICES,
        label='Tipo de Institucion',
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    description = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={
        'class': 'form-control',
    }))

    address = forms.CharField(label='Dirección', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su Dirección'
    }))

    city = forms.CharField(label='Ciudad', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su Ciudad'
    }))

    role = forms.CharField(widget=forms.HiddenInput(), initial=User.INSTITUTION)

    class Meta:
        model = Institution
        fields = ("name", "email", "password1", "password2", "idType", 'numID', 'profilePicture',
                  'city', 'address', 'type_institution', 'description')
        


class CustomAdminForm(CustomUserCreationForm):

    role=User.ADMIN
    class Meta:
        model = Admin
        fields = ("name", "email", "password1", "password2", "idType", 'numID', 'profilePicture')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", )


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo electrónico',
    }))
    password = forms.CharField(label='Contraseña', strip=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña',
        'autocomplete': 'current-password',
    }))

    error_messages = {
        'invalid_login': 'Correo electrónico o contraseña incorrectos',
        'inactive': 'Esta cuenta no está activa.',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Correo electrónico',
            'class': 'form-control',
        })
        self.fields['password'].label = ''
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Contraseña',
            'class': 'form-control',
        })
