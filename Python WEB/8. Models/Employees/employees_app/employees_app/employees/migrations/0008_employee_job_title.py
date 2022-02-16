# Generated by Django 4.0.2 on 2022-02-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_testmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.CharField(choices=[('Software engineer', 1), ('QA engineer', 2), ('DevOps specialist', 3)], default='', max_length=40),
            preserve_default=False,
        ),
    ]
