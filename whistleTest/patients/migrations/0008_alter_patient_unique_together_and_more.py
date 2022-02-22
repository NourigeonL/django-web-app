# Generated by Django 4.0.2 on 2022-02-18 04:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0007_alter_patient_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='patient',
            unique_together={('collector', 'mr_code')},
        ),
        migrations.AlterIndexTogether(
            name='patient',
            index_together={('collector', 'mr_code')},
        ),
    ]