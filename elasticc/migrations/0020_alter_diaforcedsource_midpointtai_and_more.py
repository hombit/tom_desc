# Generated by Django 4.0.6 on 2022-08-03 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elasticc', '0019_classificationmap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaforcedsource',
            name='midPointTai',
            field=models.FloatField(db_index=True),
        ),
        migrations.AlterField(
            model_name='diasource',
            name='midPointTai',
            field=models.FloatField(db_index=True),
        ),
    ]