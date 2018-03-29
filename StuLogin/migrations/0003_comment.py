# Generated by Django 2.0.3 on 2018-03-29 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StuLogin', '0002_facility'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('fid', models.CharField(db_column='FID', max_length=20)),
                ('text', models.CharField(max_length=50)),
                ('id', models.IntegerField(db_column='ID')),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
    ]
