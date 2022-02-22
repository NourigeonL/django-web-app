from distutils.command.clean import clean
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.core.exceptions import ValidationError
# Create your models here.


class Patient(models.Model):

    class Sex(models.IntegerChoices):
        UNKNOWN = 0,
        MALE = 1,
        FEMALE = 2,
        NOT_APPLICABLE = 9,

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=200, blank=True)
    health_insurance_number = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    registration_date = models.DateField(default=date.today)
    sex = models.IntegerField(choices=Sex.choices)
    mr_code = models.PositiveIntegerField()
    collector = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(blank=True, null=True,
                            allow_unicode=True)

    def __str__(self):
        return "%s_%d %s %s" % (self.collector, self.mr_code, self.last_name, self.first_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.collector.__str__() + "_" + str(self.mr_code))
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ['collector', 'mr_code']


class PatientMedicalInfo(models.Model):
    patient = models.OneToOneField(
        Patient, on_delete=models.CASCADE,
        # parent_link=True,
        primary_key=True,
    )
    hypertension = models.BooleanField(default=False)

    def __str__(self):
        return self.patient. __str__()

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)


class Image(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='images', on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    status = models.PositiveIntegerField(default=1)
    final_result = models.TextField(null=True, blank=True)
    num = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['patient', 'num']

    def __str__(self):
        return "%s_%s" % (self.patient. __str__(), self.name)

    def validate_unique(self, exclude=None):
        img = Image.objects.filter(patient=self.patient).filter(num=self.num)
        # if img is not None:
        #     raise ValidationError('tuple (patient id, num) should be unique')

    def save(self, *args, **kwargs):

        self.validate_unique()

        super(Image, self).save(*args, **kwargs)


def patient_pre_save():
    pass
