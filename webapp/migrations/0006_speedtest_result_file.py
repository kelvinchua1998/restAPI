# Generated by Django 3.0.5 on 2020-05-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_delete_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='speedtest_result',
            name='file',
            field=models.FileField(default='', null=True, upload_to='file_uploads'),
        ),
    ]
