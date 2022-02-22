from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import generic

from whistleTest.settings import DEBUG

from .models import Patient, PatientMedicalInfo, Image


def index(request):
    return HttpResponse("Patients index")


class PatientListView(LoginRequiredMixin, generic.ListView):
    model = Patient
    context_object_name = 'patient_list'
    template_name = 'patients/index.html'

    def get_queryset(self):
        return Patient.objects.filter(
            collector=self.request.user.id
        )


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Patient
    template_name = 'patients/detail.html'

    def get(self, request, pk, *args, **kwargs):
        patient = Patient.objects.get(pk=pk)
        if self.request.user.id != patient.collector.id:
            return redirect('/patients/')
        image_list = Image.objects.filter(patient=patient.id)

        return self.render_to_response({"patient": patient, "image_list": image_list})
