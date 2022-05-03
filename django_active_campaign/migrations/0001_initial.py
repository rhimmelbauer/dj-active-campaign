# Generated by Django 3.2.13 on 2022-05-02 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac_id', models.IntegerField(verbose_name='Active Campaign ID')),
                ('ac_title', models.CharField(max_length=50, verbose_name='Field Title')),
                ('ac_value', models.JSONField(verbose_name='Field Value')),
                ('required', models.BooleanField(default=False, verbose_name='Required')),
            ],
            options={
                'verbose_name': 'Custom Field',
                'verbose_name_plural': 'Custom Fields',
            },
        ),
    ]
