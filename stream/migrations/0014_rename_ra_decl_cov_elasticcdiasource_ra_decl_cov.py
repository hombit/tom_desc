# Generated by Django 3.2.11 on 2022-01-11 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0013_rename_numobjs_elasticcssobject_numobs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elasticcdiasource',
            old_name='ra_decl_cov',
            new_name='ra_decl_Cov',
        ),
    ]
