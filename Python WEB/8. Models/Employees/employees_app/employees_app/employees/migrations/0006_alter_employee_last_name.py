# Generated by Django 4.0.2 on 2022-02-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_employee_egn_alter_employee_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, default='No name', max_length=40, null=True),
        ),
    ]
