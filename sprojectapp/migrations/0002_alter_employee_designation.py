# Generated by Django 4.1.4 on 2022-12-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprojectapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Designation',
            field=models.CharField(choices=[('android developer', 'Android Developer'), ('backend developer)', 'Backend Developer')], max_length=44),
        ),
    ]
