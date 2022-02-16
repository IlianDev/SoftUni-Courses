# Generated by Django 4.0.2 on 2022-02-16 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_alter_employee_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='EGN',
            field=models.CharField(max_length=10, unique=True, verbose_name='EGN'),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employees.department'),
            preserve_default=False,
        ),
    ]