# Generated by Django 2.1.3 on 2018-12-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weloft', '0004_auto_20181223_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='Apt_address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='Apt_district',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='Apt_phoneNo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='Apt_pincode',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='Apt_state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Apt_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Flat_no',
            field=models.CharField(default='', max_length=100),
        ),
    ]
