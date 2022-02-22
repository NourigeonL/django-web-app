from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, GenericAPIView
from patients.models import Patient, PatientMedicalInfo, Image
from patients.api.serializers import PatientSerializer, ImageSerializer
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import mixins


class ApiPatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'slug'


class ApiImageViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    pagination_class = PageNumberPagination

    def list(self, request, slug):
        image_list = Image.objects.filter(patient__slug=slug)
        if image_list is not None:
            serializer = self.get_serializer(image_list, many=True)
            return Response(serializer.data)

    # def create(self, request):
    #     pass

    def retrieve(self, request, num, slug):
        print('slug = ', slug)
        print('num = ', num)
        image = Image.objects.get(num=num, patient__slug=slug)
        if image is not None:
            print("not none")
            print('image = ', image)
            serializer = self.get_serializer(image)
            print('serializer data = ', serializer.data)
            return Response(serializer.data)
        print("none")

    # # def update(self, request, pk=None):
    # #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
