from cgitb import lookup
from urllib import request
from rest_framework import serializers
from patients.models import Patient, PatientMedicalInfo, Image
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from rest_framework.reverse import reverse


class ImageHyperlink(serializers.HyperlinkedRelatedField):
    # We define these as class attributes, so we don't need to pass them as arguments.
    view_name = 'image-detail'
    queryset = Image.objects.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'slug': obj.patient.slug,
            'num': obj.num
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'patient__slug': view_kwargs['slug'],
            'num': view_kwargs['num']
        }
        return self.get_queryset().get(**lookup_kwargs)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['num', 'name', 'status', 'final_result']


class PatientMedicalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMedicalInfo
        exclude = ['patient']


class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer to Add ModelA together with ModelB
    """

    patientmedicalinfo = PatientMedicalInfoSerializer()

    images = ImageHyperlink(
        many=True,
    )

    class Meta:
        model = Patient
        exclude = ['id']
        # fields = '__all__'

    def update(self, instance, validated_data):
        medical_infos_data = validated_data.pop(
            'patientmedicalinfo')
        images_data = validated_data.pop(
            'images')

        medicalinfo = instance.patientmedicalinfo

        super().update(instance, validated_data)
        super().update(medicalinfo, medical_infos_data)

        # super().update(medicalinfo, medical_infos_data)

        print('instance = ', instance)

        for image_data in images_data:
            print("image_data = ", image_data)
            # Image.objects.filter(id=image_data.get('id')).update(**image_data)

        return instance
