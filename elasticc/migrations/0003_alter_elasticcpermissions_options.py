# Generated by Django 3.2.11 on 2022-03-28 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elasticc', '0002_elasticcpermissions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elasticcpermissions',
            options={'default_permissions': (), 'managed': False, 'permissions': (('elasticc_admin', 'Elasticc Admin User'), ('elasticc_broker', 'Can Write BrokerMessage Objects'))},
        ),
    ]
