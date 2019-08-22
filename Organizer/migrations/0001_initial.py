# Generated by Django 2.2.3 on 2019-08-22 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganiseEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=200)),
                ('event_description', models.CharField(max_length=800)),
                ('event_category', models.CharField(max_length=200)),
                ('org_name', models.CharField(max_length=200)),
                ('org_email', models.EmailField(max_length=100)),
                ('org_mobile', models.BigIntegerField()),
                ('org_contact_person', models.CharField(max_length=100)),
                ('event_poster', models.ImageField(upload_to='images/event_poster/')),
                ('event_startdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_enddate', models.DateTimeField()),
                ('us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(default=True, max_length=100)),
                ('platinum_sponsor', models.CharField(max_length=100)),
                ('f_platinum', models.TextField(max_length=1500)),
                ('ex_platinum', models.IntegerField()),
                ('gold_sponsor', models.CharField(max_length=100)),
                ('f_gold', models.TextField(max_length=1500)),
                ('ex_gold', models.IntegerField()),
                ('silver_sponsor', models.CharField(max_length=100)),
                ('f_silver', models.TextField(max_length=1500)),
                ('ex_silver', models.IntegerField()),
                ('org_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organizer.OrganiseEvent')),
                ('us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShareResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1500)),
                ('publishedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('resourceLink', models.CharField(max_length=100)),
                ('documentFile', models.FileField(upload_to='images/shared_resources_docs/')),
                ('publisedBy', models.CharField(max_length=100)),
                ('resourceImage', models.ImageField(upload_to='images/shared_resources/')),
                ('org_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organizer.OrganiseEvent')),
                ('us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=200)),
                ('expected_participant', models.IntegerField()),
                ('no_participant', models.IntegerField()),
                ('event_level', models.CharField(max_length=200)),
                ('eligibility', models.CharField(max_length=200)),
                ('prerequisite', models.TextField(max_length=1500)),
                ('facility', models.CharField(max_length=100)),
                ('event_detail_docs', models.FileField(upload_to='images/event_details_docs/')),
                ('org_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organizer.OrganiseEvent')),
                ('us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_venue_name', models.CharField(max_length=200)),
                ('event_venue_addr', models.CharField(max_length=300)),
                ('event_latitude', models.CharField(max_length=100)),
                ('event_longitude', models.CharField(max_length=100)),
                ('event_name', models.CharField(max_length=200)),
                ('eventid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organizer.OrganiseEvent')),
            ],
        ),
        migrations.CreateModel(
            name='SponsorShipDetails',
            fields=[
                ('event_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Organizer.EventDetails')),
                ('event_title', models.CharField(default=True, max_length=100)),
                ('platinum_sponsor', models.CharField(max_length=100)),
                ('f_platinum', models.TextField(max_length=1500)),
                ('ex_platinum', models.IntegerField()),
                ('gold_sponsor', models.CharField(max_length=100)),
                ('f_gold', models.TextField(max_length=1500)),
                ('ex_gold', models.IntegerField()),
                ('silver_sponsor', models.CharField(max_length=100)),
                ('f_silver', models.TextField(max_length=1500)),
                ('ex_silver', models.IntegerField()),
                ('org_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Organizer.OrganiseEvent')),
                ('us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
