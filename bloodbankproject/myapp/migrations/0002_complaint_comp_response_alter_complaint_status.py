# Generated by Django 4.0.4 on 2022-06-04 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='comp_response',
            field=models.CharField(default=' ', max_length=500),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(default='New', max_length=20),
        ),
    ]
