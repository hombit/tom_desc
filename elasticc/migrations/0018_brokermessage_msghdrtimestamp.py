# Generated by Django 4.0.6 on 2022-07-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elasticc', '0017_rename_diaobjectid_diaobjecttruth_diaobject_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brokermessage',
            name='msgHdrTimestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
