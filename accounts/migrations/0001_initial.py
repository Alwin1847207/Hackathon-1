# Generated by Django 2.1 on 2019-05-10 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=40)),
                ('confirmPassword', models.CharField(max_length=40)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]