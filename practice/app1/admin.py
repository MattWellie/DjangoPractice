from django.contrib import admin
from .models import Patient, Variant, PatientVariant, Question, Choice

admin.site.register(Patient)
admin.site.register(Variant)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(PatientVariant)