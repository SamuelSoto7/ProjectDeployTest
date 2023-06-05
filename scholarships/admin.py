from django.contrib import admin
from scholarships.models import *

# Register your models here.
admin.site.register(Scholarship)
admin.site.register(Transaction)
admin.site.register(PartialTransaction)
