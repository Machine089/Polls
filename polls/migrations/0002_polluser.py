# Generated by Django 4.0.5 on 2022-07-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('var_1', models.CharField(max_length=200)),
                ('var_2', models.CharField(max_length=200)),
            ],
        ),
    ]
