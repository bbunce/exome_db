# Generated by Django 3.2.7 on 2021-09-27 15:19

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exome_dev', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='scientist_2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='additional_seqeuncing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='analysis_completion_date',
            field=models.DateTimeField(default=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='analysis_time',
            field=models.TimeField(default=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='average_read_depth',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='coverage_20x',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='diagnosis_after_reanalysis',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='re_analysis_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_result',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('diag', 'Diagnosis'), ('likely', 'Likely diagnosis'), ('possible', 'Possible diagnosis'), ('no_diag', 'No diagnosis')], default=False, max_length=28),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_status',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('active', 'Active'), ('hold', 'Hold'), ('complete', 'Complete'), ('failed', 'Failed'), ('analysis_complete', 'Analysis Complete'), ('re_analysis', 'Re-Analysis')], default=False, max_length=57),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('trio', 'Trio'), ('singleton', 'Singleton'), ('virtual', 'Virutal')], default=False, max_length=22),
        ),
        migrations.AlterField(
            model_name='test',
            name='variant_detected_probability',
            field=models.FloatField(default=False),
        ),
    ]