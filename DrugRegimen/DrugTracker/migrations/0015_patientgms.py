# Generated by Django 3.0.4 on 2021-04-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrugTracker', '0014_patientpharmacy'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientGMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientUsername', models.CharField(max_length=50)),
                ('gms', models.CharField(max_length=50)),
            ],
        ),
    ]
