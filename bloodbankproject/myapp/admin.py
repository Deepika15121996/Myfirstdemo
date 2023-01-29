from django.contrib import admin
#from.models import *
from . import models

admin.site.register(models.BloodBank)
admin.site.register(models.Donor)
admin.site.register(models.Receiver)
admin.site.register(models.MyUser)
admin.site.register(models.Complaint)


