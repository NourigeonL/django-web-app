# Generated by Django 4.0.2 on 2022-02-17 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0005_alter_image_final_result_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(blank=True, null=True)),
                ('done_date', models.DateTimeField(null=True)),
                ('grader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.image')),
            ],
            options={
                'unique_together': {('image', 'grader')},
            },
        ),
    ]
