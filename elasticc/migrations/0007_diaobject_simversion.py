# Generated by Django 3.2.11 on 2022-04-12 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elasticc', '0006_auto_20220329_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaobject',
            name='simVersion',
            field=models.TextField(null=True),
        ),
    ]
