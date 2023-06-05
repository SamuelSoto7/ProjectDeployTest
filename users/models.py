from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

class Notification(models.Model):
    content = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    

class User(AbstractBaseUser, PermissionsMixin):
    username=None
    BENEFICIARY=1
    NATURALDONOR=2
    LEGALDONOR=3
    INSTITUTION=4
    ADMIN=5

    ROLE_CHOICE=(
          (BENEFICIARY, 'Beneficiario'),
          (NATURALDONOR,'Donante natural'),
          (LEGALDONOR,'Donante juridico'),
          (INSTITUTION,'Institución'),
          (ADMIN,'Admin'),
    )

    TI=1
    CC=2
    CE=3
    NIT=4

    IDTYPE_CHOICE= ((TI,'Tarjeta de Identidad'),
                (CC,'Cédula de Ciudadanía'),
                ( CE,'Cédula extranjera'),
                (NIT,'NIT'))
    email = models.EmailField(_("email address"), unique=True)
    name=models.CharField(max_length=100,null=False)
    profilePicture= models.ImageField(upload_to="users",null=True, blank=True)
    idType = models.PositiveSmallIntegerField(choices=IDTYPE_CHOICE,null=False)
    numID = models.CharField(max_length=10,null=False)
    role=models.PositiveSmallIntegerField(choices=ROLE_CHOICE,null=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login= models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length=15)
    notifications = models.ManyToManyField(Notification)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
   
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'idType', 'numID', 'role']

    objects = UserManager()

    def __str__(self):
        return self.email
     
    def has_module_perms(self, app_label):
       return self.is_superuser
    def has_perm(self, perm, obj=None):
       return self.is_superuser
    def get_full_name(self):
        return self.name
    
class Admin(User):
    pass
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Admin'

class NaturalDonor(User):
    pass

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'NaturalDonor'

class LegalDonor(User):
    description = models.TextField(max_length=255)
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
    organization_type = models.CharField(
        max_length=50,
        choices=organization_type_choices,
    )


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'LegalDonor'

class Beneficiary(User):
    # beneficiary specific fields
    birth_date = models.DateField()
    optionsGender = (('F','Femenino'),
                     ('M','Masculino'),
                     ('O','Otro'))
    gender = models.CharField(max_length=15,choices=optionsGender,null=False) 

    def __str__(self):
        return self.name + " email: " + self.email    
    
    class Meta:
        verbose_name = 'Beneficiary'
        verbose_name_plural = 'Beneficiaries'


class Institution(User):

    description = models.TextField(max_length=255)
    TYPE_CHOICES = (
        ('Tecnica', 'Tecnica'),
        ('Tecnologica', 'Tecnologica'),
        ('Pregrado', 'Pregrado'),
        ('Posgrado','Posgrado')
    )
    type_institution = models.CharField(
        max_length=255,
        blank = False,
    )
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=70)
    money_donation = models.IntegerField(default=0)

    optionsstate= (('A','Aprobada'),
                     ('P','Pendiente'),
                     ('R','Rechazada'))
    verificationState = models.CharField(max_length=30,choices=optionsstate,null=False, default='P')


   