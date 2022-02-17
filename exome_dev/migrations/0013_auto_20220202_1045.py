# Generated by Django 3.2.7 on 2022-02-02 10:45

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exome_dev', '0012_patient_proband'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family_Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workbatch_id', models.CharField(max_length=10, unique=True)),
                ('test_activation_date', models.DateTimeField(blank=True)),
                ('library_prep_date', models.DateTimeField(blank=True)),
                ('sample_sent_date', models.DateTimeField(blank=True)),
                ('sample_received_date', models.DateTimeField(blank=True)),
                ('test_status', multiselectfield.db.fields.MultiSelectField(choices=[('logged', 'Logged'), ('active', 'Active'), ('hold', 'Hold'), ('complete', 'Complete'), ('failed', 'Failed'), ('analysis_complete', 'Analysis Complete'), ('re_analysis', 'Re-Analysis')], default=False, max_length=64)),
                ('analysis_completion_date', models.DateTimeField(blank=True)),
                ('analysis_time', models.TimeField(blank=True)),
                ('average_read_depth', models.IntegerField(blank=True)),
                ('coverage_20x', models.IntegerField(blank=True)),
                ('variant_detected_probability', models.FloatField(blank=True)),
                ('re_analysis_required', models.BooleanField(blank=True, default=False)),
                ('diagnosis_after_reanalysis', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='family',
            name='workbatch_id',
        ),
        migrations.RemoveField(
            model_name='test',
            name='analysis_completion_date',
        ),
        migrations.RemoveField(
            model_name='test',
            name='analysis_time',
        ),
        migrations.RemoveField(
            model_name='test',
            name='average_read_depth',
        ),
        migrations.RemoveField(
            model_name='test',
            name='coverage_20x',
        ),
        migrations.RemoveField(
            model_name='test',
            name='diagnosis_after_reanalysis',
        ),
        migrations.RemoveField(
            model_name='test',
            name='library_prep_date',
        ),
        migrations.RemoveField(
            model_name='test',
            name='re_analysis_required',
        ),
        migrations.RemoveField(
            model_name='test',
            name='sample_received_date',
        ),
        migrations.RemoveField(
            model_name='test',
            name='sample_sent_date',
        ),
        migrations.RemoveField(
            model_name='test',
            name='test_activation_date',
        ),
        migrations.RemoveField(
            model_name='test',
            name='test_result',
        ),
        migrations.RemoveField(
            model_name='test',
            name='test_status',
        ),
        migrations.RemoveField(
            model_name='test',
            name='variant_detected_probability',
        ),
        migrations.CreateModel(
            name='variant_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exome_dev.family_tests')),
                ('variant_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exome_dev.variant')),
            ],
        ),
        migrations.AddField(
            model_name='family_tests',
            name='family_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exome_dev.family'),
        ),
        migrations.AddField(
            model_name='family_tests',
            name='test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exome_dev.test'),
        ),
        migrations.CreateModel(
            name='Clinician_Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinician_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exome_dev.clinician')),
                ('family_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exome_dev.family')),
            ],
        ),
    ]
