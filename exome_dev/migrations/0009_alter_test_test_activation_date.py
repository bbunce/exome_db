# Generated by Django 3.2.7 on 2022-02-02 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exome_dev', '0008_auto_20220202_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_activation_date',
            field=models.DateTimeField(null=True),
        ),
    ]
