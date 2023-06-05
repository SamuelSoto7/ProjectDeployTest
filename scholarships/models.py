from django.db import models
from users.models import Beneficiary, Institution, NaturalDonor, User
# Create your models here.

# Create your models here.

class Scholarship(models.Model):
    stratum = models.CharField(max_length=2,null=False)
    photocopy_id = models.FileField(upload_to="files/",null=False, blank=False)
    motivational_letter = models.TextField(max_length=2000,null=False)
    certificate = models.FileField(upload_to="files/",null=False, blank=False)
    value_period = models.IntegerField(null=False)
    icfes_score = models.IntegerField(null=False)
    period_current = models.IntegerField(null=False)
    program_adm = models.CharField(max_length=40,null=False)    
    optionsapplication = (('NI','Nuevo Ingreso'),
              ('A','Antiguo'))
    application_type = models.CharField(max_length=40,choices=optionsapplication,null=False)
    optionsstate = (('P','Pendiente'),
                     ('A','Aceptada'),
                     ('R','Rechazada'))
    state = models.CharField(max_length=30,choices=optionsstate,null=False)
    total_periods = models.IntegerField(null=False)
    optionsactive = (('AC','Activo'),
                     ('IN','Inactivo'))
    active = models.CharField(max_length=20,choices=optionsactive,default='Activo',null=False)
    date_application = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(Beneficiary,null=False,blank=False,on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution,null=False,blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_user} - {self.institution} - {self.period_current}"
    

class Transaction(models.Model):
    date_transaction = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    payment = models.CharField(max_length=120) 
    optionspay = (('PSE','PSE'),
                              ('Cards','Card'),
                                   ('PayPal','PayPal'))
     
    type_pay = models.CharField(max_length=200,choices=optionspay,null=False) 

    # relation with User donor
   
    donor_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, related_name="donator")

    # optional relation with Transaction  
    scolarship_donation = models.ForeignKey(Scholarship, on_delete=models.CASCADE, null=True, blank=True, related_name='donations')

    # optional relation with Institution
    institution_donation = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True, related_name='donations')


class PartialTransaction(models.Model):
    date_transaction = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    payment = models.CharField(max_length=120) 
    optionspay = (
        ('PSE', 'PSE'),
        ('Cards', 'Card'),
        ('PayPal', 'PayPal')
    )
    type_pay = models.CharField(max_length=200, choices=optionspay, null=True)
    donor_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="partialtransaction_donator")
    scolarship_donation = models.ForeignKey(Scholarship, on_delete=models.CASCADE, null=True, blank=True, related_name='partialtransaction_donations')
    institution_donation = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True, related_name='partialtransaction_donations')
   
    #Notificaciones


