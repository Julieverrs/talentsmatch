# Generated by Django 4.2 on 2024-11-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpostings', '0004_jobposting_delete_applicant_delete_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='experience_level',
            field=models.IntegerField(),
        ),
    ]
