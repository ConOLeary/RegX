# Generated by Django 3.0.4 on 2021-03-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrugTracker', '0007_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoseURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doseURL', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Videos',
        ),
    ]
