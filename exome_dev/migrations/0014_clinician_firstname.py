# Generated by Django 3.2.7 on 2022-02-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exome_dev', '0013_auto_20220202_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinician',
            name='firstname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
