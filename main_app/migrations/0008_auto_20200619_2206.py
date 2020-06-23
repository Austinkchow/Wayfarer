# Generated by Django 3.0.7 on 2020-06-19 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200619_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(choices=[('L', 'London'), ('S', 'Sydney'), ('SF', 'San Francisco'), ('SE', 'Seattle')], default=(('L', 'London'), ('S', 'Sydney'), ('SF', 'San Francisco'), ('SE', 'Seattle')), max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
