# Generated by Django 3.1.5 on 2021-03-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0006_userdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='zipcode',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
