# Generated by Django 3.2.13 on 2022-10-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('re_pair', '0002_inform'),
    ]

    operations = [
        migrations.AddField(
            model_name='inform',
            name='opendate',
            field=models.DateField(null=True),
        ),
    ]
