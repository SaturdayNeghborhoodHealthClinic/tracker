# Generated by Django 3.0.5 on 2020-05-10 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pttrack', '0001_initial'),
        ('followup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccinefollowup',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='vaccinefollowup',
            name='author_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.ProviderType'),
        ),
        migrations.AddField(
            model_name='vaccinefollowup',
            name='contact_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.ContactMethod'),
        ),
        migrations.AddField(
            model_name='vaccinefollowup',
            name='contact_resolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='vaccinefollowup',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.Patient'),
        ),
        migrations.AddField(
            model_name='referralfollowup',
            name='apt_location',
            field=models.ForeignKey(blank=True, help_text='Where is the appointment?', null=True, on_delete=django.db.models.deletion.PROTECT, to='pttrack.ReferralLocation'),
        ),
        migrations.AddField(
            model_name='referralfollowup',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='referralfollowup',
            name='author_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.ProviderType'),
        ),
        migrations.AddField(
            model_name='referralfollowup',
            name='contact_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.ContactMethod'),
        ),
        migrations.AddField(
            model_name='referralfollowup',
            name='contact_resolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='referralfollowup',
            name='noapt_reason',
            field=models.ForeignKey(blank=True, help_text="If the patient didn't make an appointment, why not?", null=True, on_delete=django.db.models.deletion.PROTECT, to='followup.NoAptReason'),
        ),
        migrations.AddField(
            model_name='referralfollowup',
            name='noshow_reason',
            field=models.ForeignKey(blank=True, help_text="If the patient didn't go to appointment, why not?", null=True, on_delete=django.db.models.deletion.PROTECT, to='followup.NoShowReason'),
        ),
        migrations.AddField(
            model_name='referralfollowup',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.Patient'),
        ),
        migrations.AddField(
            model_name='referralfollowup',
            name='referral_type',
            field=models.ForeignKey(blank=True, help_text='What kind of provider was the patient referred to?', null=True, on_delete=django.db.models.deletion.PROTECT, to='pttrack.ReferralType'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='author_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.ProviderType'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='contact_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.ContactMethod'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='contact_resolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='followup.ContactResult'),
        ),
        migrations.AddField(
            model_name='labfollowup',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pttrack.Patient'),
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='author',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='author_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ProviderType'),
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='contact_method',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ContactMethod'),
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='contact_resolution',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='followup.ContactResult'),
        ),
    ]
