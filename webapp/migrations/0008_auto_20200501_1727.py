# Generated by Django 3.0.5 on 2020-05-01 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20200501_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speedtest_result',
            name='timestamp',
            field=models.CharField(max_length=30),
        ),
    ]