# Generated by Django 3.2.11 on 2022-02-02 17:54
# Manually edited by RKNOP 2022-02-02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql=( "CREATE INDEX target_q3c_radec_idx ON stream_target "
                  "USING btree(q3c_ang2ipix(right_ascension, declination))" ),
            reverse_sql="DROP INDEX target_q3c_radex_idx"
        ),
        migrations.RunSQL(
            sql="CREATE INDEX alert_q3c_radec_idx ON stream_alert USING btree(q3c_ang2ipix(ra, decl))",
            reverse_sql="DROP INDEX alert_q3c_radex_idx"
        ),
        migrations.RunSQL(
            sql=( "CREATE INDEX elasticcdiaobject_q3c_radec_idx ON stream_elasticcdiaobject "
                  "USING btree(q3c_ang2ipix(ra, decl))" ),
            reverse_sql="DROP INDEX elasticcdiaobject_q3c_radex_idx"
        ),
        migrations.RunSQL(
            sql=( "CREATE INDEX elasticcdiasource_q3c_radec_idx ON stream_elasticcdiasource "
                  "USING btree(q3c_ang2ipix(ra, decl))" ),
            reverse_sql="DROP INDEX elasticcdiasource_q3c_radex_idx"
        ),
    ]
