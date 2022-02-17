# Generated by Django 3.2.7 on 2022-02-01 15:40

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exome_dev', '0004_auto_20220112_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel_name', models.CharField(max_length=50)),
                ('date_added', models.DateField()),
                ('submitter', models.CharField(max_length=20)),
                ('on_panelapp', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build', multiselectfield.db.fields.MultiSelectField(choices=[('37', 'GRCh37'), ('38', 'GRCh38')], default='37', max_length=5, null=True)),
                ('chromosome', models.CharField(blank=True, max_length=2, null=True)),
                ('gene', models.CharField(blank=True, max_length=100, null=True)),
                ('transcript', models.CharField(blank=True, max_length=100, null=True)),
                ('genomic', models.CharField(blank=True, max_length=100, null=True)),
                ('dna', models.CharField(blank=True, max_length=100, null=True)),
                ('protein', models.CharField(blank=True, max_length=100, null=True)),
                ('zygosity', models.CharField(blank=True, max_length=100, null=True)),
                ('vus_wip', models.BooleanField(default=False)),
                ('pubmed_ref', models.IntegerField()),
                ('gene_matcher', models.BooleanField(default=False)),
                ('var_prev_reported', models.CharField(blank=True, max_length=100, null=True)),
                ('var_type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('miss', 'Missense'), ('non', 'Nonsense'), ('syn', 'Synonymous'), ('del', 'Deletion in-frame'), ('del_fs', 'Deletion frameshift'), ('dup', 'Duplication in-frame'), ('dup_fs', 'Duplication frameshift'), ('part_del', 'Partial gene deletion'), ('whole_del', 'Whole gene deletion'), ('part_dup', 'Partial gene duplication'), ('whole_dup', 'Whole gene duplication'), ('splicing', 'Splicing'), ('regulatory', 'Regulatory')], max_length=92, null=True)),
                ('primary_additinal_var', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='family',
            name='referral_reason',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='patient',
            name='exome_id',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nhs_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('active', 'Active'), ('on_hold', 'On hold'), ('complete', 'Complete')], max_length=23),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workbatch_id', models.IntegerField(unique=True)),
                ('test_type', multiselectfield.db.fields.MultiSelectField(choices=[('trio', 'Trio'), ('singleton', 'Singleton'), ('virtual', 'Virutal')], default=False, max_length=22, null=True)),
                ('test_status', multiselectfield.db.fields.MultiSelectField(choices=[('logged', 'Logged'), ('active', 'Active'), ('hold', 'Hold'), ('complete', 'Complete'), ('failed', 'Failed'), ('analysis_complete', 'Analysis Complete'), ('re_analysis', 'Re-Analysis')], default=False, max_length=64, null=True)),
                ('test_result', multiselectfield.db.fields.MultiSelectField(choices=[('diag', 'Diagnosis'), ('likely', 'Likely diagnosis'), ('possible', 'Possible diagnosis'), ('no_diag', 'No diagnosis')], default='Logged', max_length=28)),
                ('test_activation_date', models.DateTimeField()),
                ('library_prep_date', models.DateTimeField()),
                ('sample_sent_date', models.DateTimeField()),
                ('sample_received_date', models.DateTimeField()),
                ('additional_seqeuncing', models.BooleanField(default=False)),
                ('analysis_completion_date', models.DateTimeField(default=False)),
                ('analysis_time', models.TimeField(default=False)),
                ('average_read_depth', models.IntegerField(default=False)),
                ('coverage_20x', models.IntegerField(default=False)),
                ('variant_detected_probability', models.FloatField(default=False)),
                ('re_analysis_required', models.BooleanField(default=False)),
                ('diagnosis_after_reanalysis', models.BooleanField(default=False)),
                ('family_id', models.ManyToManyField(to='exome_dev.Family')),
                ('panel_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exome_dev.panel')),
            ],
        ),
    ]
