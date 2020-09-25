# Generated by Django 3.1 on 2020-08-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='company',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
