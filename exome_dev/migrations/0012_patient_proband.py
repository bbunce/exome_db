# Generated by Django 3.2.7 on 2022-02-02 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exome_dev', '0011_alter_test_test_activation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='proband',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
