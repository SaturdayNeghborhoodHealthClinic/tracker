# Generated by Django 3.0.5 on 2020-05-10 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pttrack', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followup', '0002_auto_20200509_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='patient',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Patient'),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='apt_location',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Where is the appointment?', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ReferralLocation'),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='author',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='author_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ProviderType'),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='contact_method',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ContactMethod'),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='contact_resolution',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='noapt_reason',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text="If the patient didn't make an appointment, why not?", null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='followup.NoAptReason'),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='noshow_reason',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text="If the patient didn't go to appointment, why not?", null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='followup.NoShowReason'),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='patient',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Patient'),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='referral_type',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='What kind of provider was the patient referred to?', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ReferralType'),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='author',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='author_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ProviderType'),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='contact_method',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ContactMethod'),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='contact_resolution',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='patient',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Patient'),
        ),
        migrations.AddField(
            model_name='historicalgeneralfollowup',
            name='author',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='historicalgeneralfollowup',
            name='author_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ProviderType'),
        ),
        migrations.AddField(
            model_name='historicalgeneralfollowup',
            name='contact_method',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ContactMethod'),
        ),
        migrations.AddField(
            model_name='historicalgeneralfollowup',
            name='contact_resolution',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='historicalgeneralfollowup',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalgeneralfollowup',
            name='patient',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Patient'),
        ),
        migrations.AddField(
            model_name='generalfollowup',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='generalfollowup',
            name='author_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.ProviderType'),
        ),
        migrations.AddField(
            model_name='generalfollowup',
            name='contact_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.ContactMethod'),
        ),
        migrations.AddField(
            model_name='generalfollowup',
            name='contact_resolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='generalfollowup',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.Patient'),
        ),
    ]