# Generated by Django 3.1.5 on 2021-03-11 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.IntegerField()),
                ('p_animalpic', models.ImageField(default='animalpic/default.jpg', upload_to='animalpic')),
                ('p_name', models.CharField(max_length=12)),
                ('p_type', models.CharField(max_length=20)),
                ('p_breed', models.CharField(max_length=20)),
                ('p_age', models.IntegerField()),
                ('p_location', models.CharField(default='None', max_length=50)),
                ('p_gender', models.CharField(max_length=7)),
                ('p_vaccination', models.CharField(max_length=4)),
                ('p_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('evaluation_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('admin_id', models.IntegerField()),
                ('animal_id', models.IntegerField()),
                ('type', models.CharField(default=None, max_length=10)),
                ('pickup_id', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('eval_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoption.evaluation')),
            ],
        ),
    ]
