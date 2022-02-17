from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Family)
admin.site.register(Contact_Log)
admin.site.register(Test)
admin.site.register(Family_Test)
admin.site.register(Panel)
admin.site.register(Variant)
admin.site.register(Variant_Test)
admin.site.register(Clinician)
admin.site.register(Clinician_Family)

