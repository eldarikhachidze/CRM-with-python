# Generated by Django 5.1.1 on 2024-09-12 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_rename_flot_table_close_flot_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='active',
        ),
        migrations.AddField(
            model_name='table',
            name='close_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
