# Generated by Django 3.2.7 on 2022-02-02 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exome_dev', '0009_alter_test_test_activation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_activation_date',
            field=models.DateTimeField(),
        ),
    ]