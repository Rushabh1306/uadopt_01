# Generated by Django 3.1.5 on 2021-03-29 05:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('adoption', '0010_delete_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='answer1',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='answer10',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='answer2',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='answer3',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='answer4',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='answer5',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='answer6',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='answer7',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='answer8',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='answer9',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]