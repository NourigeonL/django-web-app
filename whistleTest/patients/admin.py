from django.contrib import admin
from .models import Patient, PatientMedicalInfo, Image
from django.core.exceptions import ObjectDoesNotExist
# Register your models here.


class PatientMedicalInfoInLine(admin.StackedInline):
    model = PatientMedicalInfo


class ImageInLine(admin.TabularInline):
    model = Image
    # readonly_fields = ["final_result"]


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    inlines = [PatientMedicalInfoInLine, ImageInLine]
    readonly_fields = ["slug"]

    def save_model(self, request, obj, form, change):
        patient = form.save()
        try:
            infos = patient.patientmedicalinfo
        except ObjectDoesNotExist:
            infos = PatientMedicalInfo(patient=patient)
            infos.save()
